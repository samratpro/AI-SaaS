from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', views.dashboard, name='dashboard'),  
    path('website_list/', views.website, name='website_list'), 
    path('single_website_view/<website_id>', views.single_website_view, name='single_website_view'),  
    path('update_website/<website_id>', views.update_website, name='update_website'), 
    path('delete_website/<website_id>', views.delete_website, name='delete_website'), 
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)