from django.test import TestCase

keyword = 'keyword  knalncf'
clean_heading = 'clean_heading dsd '

from random import choice

paragraph_prompt = '''
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




i = 3
while i > 0:
    para_prompt = choice(paragraph_prompt.split('<<prompt separator>>')).replace('<<keyword>>', keyword).replace('<<heading>>', clean_heading)
    print(para_prompt)
    i -= 1

