from django.db import models
from userapp.models import *
# Create your models here.



title = '''
Write an SEO title on this keyword within 55 characters and the keyword must be directly included in the title.
keyword:  <<keyword>>
'''

Outline_prompt = '''
Write outline on this topic <<keyword>>
outline must be H2: format, not underscore, not symbol, not hyphen, not number and no indentation, under each H2 : will have 4 H3 : not need sub heading for H3 :
and an important command is, outlines not answer
and another important command is, do not give me "Introduction" and "Conclusion, each heading length must be less than 7 words.
H1: <<keyword>>
'''
Introduction = '''
Write a article introduction on this keyword intro start with technical terms, not like """are you""" and keyword must be include in output do not give me direct solution in intro section, intro last sentence must be interesting to read the full article, keyword: <<keyword>>
and length approx. 100 words
'''
H2_title = '''
Write an h2 heading on this keyword within 55 characters before starting the main article and the keyword must be directly included in the title.
keyword: <<keyword>>
'''
Paragraph_prompt = '''
Make sure that you dont follow Ai pattern but article should be really simple and it should make sense. it should be as written with an intermediate level writer, make sure to add a bit of humor and add some funny lines. also on keypoints, you can add <em></em>, if necessary: Write article paragraph section from this heading, interesting, and organized way like human writing but not unnecessary words not long length!
the article title of this paragraph is : <<keyword>>,
paragraph heading is : <<heading>>
Each output sentence will be short, meaningful and easy to read, that can understand elementary school student.
you can add bullet points or table in the section, if its suitable, the bullet points and tables must with <ul><li> tags or <table></table> tag and paragraph is with <p></p> tags 

<<prompt separator>>

Make sure that you dont follow Ai pattern but article should be really simple and it should make sense. it should be as written with an intermediate level writer, make sure to add a bit of humor and add some funny lines. also on keypoints, you can add <em></em>,  if necessary: Write article paragraph section from this heading, interesting, and organized way like human writing but not unnecessary words not long length!
the article title of this paragraph is : <<keyword>>,
paragraph heading is : <<heading>>
please add a html table in the section, if its suitable, tables must with html <table></table> tag and paragraph is with <p></p> tags.
'''

Faq_question = '''
Topic: <<keyword>>
Write 5 related questions on this topic
1.
'''

Faq_ans = '''
Write a short answer to this question within four sentence <<question>>
'''

Summary = '''
Write a short briefing before starting the main article after intro,
Keyword: <<keyword>>
Must be include keyword in output.
and length approx. 120 words
'''

Conclusion_para = '''
keyword: <<keyword>>
Write an web article bottom summary\n and length approx. 60 words
'''

Excerpt = '''
Write a short summary,
Keyword: <<keyword>>,
Must be include keyword in output
and length approx. 25 words
'''


class info_bulk_model(models.Model):
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE, null=True, blank=True)
    keyword_name = models.CharField(max_length=100)
    status = models.CharField(max_length=20, default='Pending')
    error = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.keyword_name
    

class Info_bulk_Command(models.Model):
    title = models.TextField(null=True, blank=True, default=title)
    outline_prompt = models.TextField(null=True, blank=True, default=Outline_prompt)
    introduction = models.TextField(null=True, blank=True, default=Introduction)
    h2_title = models.TextField(null=True, blank=True, default=H2_title)
    paragraph_prompt = models.TextField(null=True, blank=True, default=Paragraph_prompt)
    faq_question = models.TextField(null=True, blank=True, default=Faq_question)
    faq_ans = models.TextField(null=True, blank=True, default=Faq_ans)
    summary = models.TextField(null=True, blank=True, default=Summary)
    conclusion_para = models.TextField(null=True, blank=True, default=Conclusion_para)
    excerpt = models.TextField(null=True, blank=True, default=Excerpt)
    

    def __str__(self):
        return 'Info tools bulk posting commands'

    

class Info_Manual_Command(models.Model):
    generate_title = models.TextField(null=True, blank=True)
    generate_outline = models.TextField(null=True, blank=True)
    generate_paragraph = models.TextField(null=True, blank=True)

    def __str__(self):
        return 'Info tools manual posting commands'