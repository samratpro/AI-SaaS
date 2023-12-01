from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from dashapp.models import *
from openai import OpenAI
from django.db.models import F
from infoapp.models import *





def text_render(previous_prompt, prompt):
        while True:
            api= ApiList.objects.filter(filled_quota__lt=F('website_quota_limit')).first()
            print('bulk info , type(api) : ', type(api))
            print('bulk info , api : ', api)
            print('bulk info ,api.filled_quota : ', api.filled_quota)
            if api != None:
                api.filled_quota += 1
                break
        try:
            client = OpenAI(api_key=api.api_key)
            print('prompts ', prompt)
            response = client.chat.completions.create(
                messages=[
                    {"role": "system", "content": previous_prompt},
                    {"role": "user","content": prompt}
                    ],
                    model="gpt-3.5-turbo",
                )
            print('bulk info ,api.filled_quota : ', api.filled_quota)
            api.filled_quota -= 1
            print('bulk info ,api.filled_quota : ', api.filled_quota)
            return response.choices[0].message.content
        except Exception as oops:
            api.error_status = 'Error Message from OpenAI server : ' + str(oops)
            api.save()
            pass
        return 'API Error From Server'



def formated_outline(keyword):
        bulk_Command = Info_bulk_Command.objects.all().first()
        print('Outline Formating...')
        print(" bulk_Command.outline_prompt :  ", bulk_Command.outline_prompt)
        i = 1
        while True:
            outline = text_render('', bulk_Command.outline_prompt.replace('<<keyword>>', keyword))
            print(f' Outline Loop {i} : ', outline) 
            i += 1
            if 'h2' in outline or 'H2' in outline or outline == 'openaierror':   # openaierror is for breaking unlimited loop if API error
                break
        outlines = list()
        return outline
        # print('Outline Raw : ', outlines)
        # for line in outline.splitlines():
        #     if len(line) > 1 and not 'introduction' in line.lower() and not 'objective' in line.lower() and not 'conclusion' in line.lower():
        #         if 'h2' in line.lower():
        #             line_format = line.replace('H2','').replace('h2','').replace(':','').replace('-','').strip()
        #             if len(line_format) > 0:
        #                 outlines.append('<h3>'+line_format.capitalize()+'</h3>')
        #         else:
        #             line_format = line.replace('H3','').replace('h3','').replace(':','').replace('-','').strip()
        #             if len(line_format) > 0:
        #                 outlines.append('<h4>'+line_format.capitalize()+'</h4>')
        # print('Outline Formating done...')
        # return outlines



class GenerateInfoTitleTextView(APIView):
    def post(self, request):
        if request.user.is_authenticated:
            serializer = Generate_Info_Title_Serializer(data=request.data)
            if serializer.is_valid():
                input_text = serializer.validated_data['input_text']
                generated_text = text_render('', input_text).replace('"','')
                return Response({'generated_text': generated_text}, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GenerateInfoOutlineTextView(APIView):
    def post(self, request):
        if request.user.is_authenticated:
            serializer = Generate_Info_Outline_Serializer(data=request.data)
            if serializer.is_valid():
                input_text = serializer.validated_data['input_text']
                generated_text = formated_outline(input_text)
                return Response({'generated_text': generated_text}, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

