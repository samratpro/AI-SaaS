from django.urls import path
from .views import *

urlpatterns = [
path('generate-info-single-title/', GenerateInfoTitleTextView.as_view(), name='generate_info_single_title'),
path('generate-info-single-outline/', GenerateInfoOutlineTextView.as_view(), name='generate_info_single_outline'),
]