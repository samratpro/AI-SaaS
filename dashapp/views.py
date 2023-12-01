from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *

# Create your views here.



'''Website'''
@login_required(login_url='login/')
def website(request):

        website_data = Website_List.objects.filter(user=request.user)

        template = 'dashboard/website.html'
        if request.method == 'POST':
            website_name = request.POST['website_name']
            website_url = request.POST['website_url']
            username = request.POST['username']
            app_pass = request.POST['app_pass']
            obj = Website_List(user=request.user, website_name=website_name, website_url=website_url, username=username, application_password=app_pass)
            obj.save()
            return redirect('/website_list')
                
        else:
            context = {'website_data':website_data}
            return render(request, template, context=context)


@login_required(login_url='login/')  # login/  is custom login URL path
def single_website_view(request, website_id):   # ```data_id``` should be pass in url as <data_id>
    template = "dashboard/single_website_view.html"
    sigle_website_data = Website_List.objects.get(pk=website_id, user=request.user)         # we can't use `id` as function argument
    context = {'sigle_website_data': sigle_website_data,'website_id': website_id}   # data id for editing request
    return render(request, template, context)


@login_required(login_url='login/') 
def update_website(request, website_id):
        template = "dashboard/update_website.html"
        website = Website_List.objects.get(pk=website_id, user=request.user)

        if request.method == "POST":
                website.website_name = request.POST['website_name']
                website.website_url = request.POST['website_url']
                website.username = request.POST['username']
                website.app_pass = request.POST['app_pass']
                website.save()
                return redirect('/website_list')
        else:
            context = {'existing_website_data': website,'website_id': website_id}
        return render(request, template, context)


@login_required(login_url='login/') 
def delete_website(request, website_id):
        website = Website_List.objects.get(pk=website_id, user=request.user)
        website.delete()
        return redirect('/website_list')




''' Youtube API '''
@login_required(login_url='login/')
def youtubeapi(request):

        youtubeapi_data = Youtube_api.objects.filter(user=request.user)

        template = 'dashboard/youtubeapi.html'
        if request.method == 'POST':
            apiname = request.POST['apiname']
            apikey = request.POST['apikey']
            obj = Youtube_api(user=request.user, name=apiname, API_Key=apikey)
            obj.save()
            return redirect('/youtubeapi_list')
                
        else:
            context = {'youtubeapi_data':youtubeapi_data}
            return render(request, template, context=context)



@login_required(login_url='login/') 
def update_youtubeapi(request, youtubeapi_id):
        template = "dashboard/update_youtubeapi.html"
        youtubeapi =Youtube_api.objects.get(pk=youtubeapi_id, user=request.user)

        if request.method == "POST":
                youtubeapi.name = request.POST['apiname']
                youtubeapi.API_Key = request.POST['apikey']
                youtubeapi.save()
                return redirect('/youtubeapi_list')
        else:
            context = {'existing_youtubeapi_data': youtubeapi,'youtubeapi_id': youtubeapi_id}
        return render(request, template, context)


@login_required(login_url='login/') 
def delete_youtubeapi(request, youtubeapi_id):
        youtubeapi = Youtube_api.objects.get(pk=youtubeapi_id, user=request.user)
        youtubeapi.delete()
        return redirect('/youtubeapi_list')








@login_required(login_url='login/')
def dashboard(request):
    template = 'dashboard/dashboard.html'
    count_website = Website_List.objects.filter(user=request.user).count()

    context = {'count_website':count_website,}
    return render(request, template, context=context)