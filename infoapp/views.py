from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from dashapp.models import *
from django.db.models import F
from infoapp.models import *
import threading
from .task import *

# Create your views here.



scheduler_thread = None
@login_required(login_url='login/')   
def bulk_posting(request):
        template = 'infoapp/bulkposting.html'
        curent_user = request.user
        website = Website_List.objects.filter(user=curent_user)
        youtubeapi = Youtube_api.objects.filter(user=curent_user)
        keyword_pending = info_bulk_model.objects.filter(user=curent_user, status='Pending')
        keyword_completed = info_bulk_model.objects.filter(user=curent_user, status='Completed')
        keyword_faild = info_bulk_model.objects.filter(user=curent_user, status='Failed')
        context = {'keyword_pending': keyword_pending, 'youtubeapi':youtubeapi, 
                   'website':website, 'keyword_completed':keyword_completed,
                   'keyword_faild':keyword_faild
                   }
        
        if request.method == 'POST':
            try:
                keyword_list = request.POST.get('keyword_list')
                keywords = keyword_list.split('\n')
                
                website_id = request.POST['website_id']
                url = Website_List.objects.get(pk=website_id).website_url
                username = Website_List.objects.get(pk=website_id).username
                app_pass = Website_List.objects.get(pk=website_id).application_password
                
                try:
                    youtubeapi_id = request.POST['youtubeapi_id']
                    youtube_key = Youtube_api.objects.get(pk=youtubeapi_id).API_Key 
                except:
                    youtube_key = ''
                
                category = request.POST['category']
                status = request.POST['status']
                
                print('website_url : ',url)
                print('website_username : ',username)
                print('website_app_pass : ',app_pass)
                print('youtube_api_key : ',youtube_key)
                print('category : ', category)
                print('status : ', status)
                
                for keyword in keywords:
                    keyword = keyword.strip()
                    if keyword:
                        info_bulk_model.objects.create(user=request.user,keyword_name=keyword, status='Pending')

                global scheduler_thread
                if scheduler_thread is None or not scheduler_thread.is_alive():
                    # Start the task scheduler in a separate thread
                    scheduler_thread = threading.Thread(target=BulkKeywordsJob, args=(curent_user,url, username, app_pass, youtube_key, category, status))
                    scheduler_thread.start()
                return redirect('info_bulk_posting')
            except:
                return redirect('info_bulk_posting')
        else:
            return render(request, template, context=context)





@login_required(login_url='login/')     
def single_posting(request):
        website = Website_List.objects.filter(user=request.user)
        openai_key = ApiList.objects.all()
        less_quota_data = ApiList.objects.filter(filled_quota__lt=F('website_quota_limit'))
        youtubeapi = Youtube_api.objects.filter(user=request.user)
        prompts = Info_Manual_Command.objects.first()
        context = {'website':website, 'youtubeapi':youtubeapi, 'prompts':prompts}
        template = 'infoapp/singlepost.html'
        # if request.method == 'POST':
        #     try:
        #         keyword = request.POST['keyword']
        #         outline = request.POST['outline']
        #         website_id = request.POST['website_id']
        #         url = WesiteModel.objects.get(pk=website_id).website_url
        #         username = WesiteModel.objects.get(pk=website_id).username
        #         app_pass = WesiteModel.objects.get(pk=website_id).app_pass
                
        #         openaiapi_id = request.POST['openaiapi_id']
        #         openai_key = OpenaiAPIModel.objects.get(pk=openaiapi_id).API_Key
        #         openai_engine = OpenaiAPIModel.objects.get(pk=openaiapi_id).engine
                
        #         try:
        #             youtubeapi_id = request.POST['youtubeapi_id']
        #             youtube_key = YoutubeAPIModel.objects.get(pk=youtubeapi_id).API_Key 
        #         except:
        #             youtube_key = ''
                
        #         category = request.POST['category']
        #         status = request.POST['status']
                
        #         SingleKeywordModel.objects.create(name=keyword, outline=outline, status='Pending')
                
        #         print('website_url : ',url)
        #         print('website_username : ',username)
        #         print('website_app_pass : ',app_pass)
        #         print('openai_api_key : ',openai_key)
        #         print('youtube_api_key : ',youtube_key)
        #         print('category : ', category)
        #         print('status : ', status)
        #         print('openai_engine : ', openai_engine)
                
        #         global scheduler_thread2
        #         if scheduler_thread2 is None or not scheduler_thread2.is_alive():
        #               # Start the task scheduler in a separate thread
        #               scheduler_thread2 = threading.Thread(target=SingleKeywordsJob, args=(url, username, app_pass, openai_key, openai_engine, youtube_key, category, status))
        #               scheduler_thread2.start()
        #         return redirect('info_single_posting')
        #     except:
        #         return redirect('info_single_posting')
        # else:   
        #     redirect('info_single_posting')
            
        return render(request, template, context=context)


