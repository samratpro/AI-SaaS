from django.urls import path
from .views import *

urlpatterns = [
path('generate-text/', GenerateTextView.as_view(), name='generate_text'),
]