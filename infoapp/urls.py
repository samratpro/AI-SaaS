# URL Mapping in App URL file----------------------
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('bulk-posting', views.bulk_posting, name='info_bulk_posting'),  
    path('completed-info-bulk-post', views.completed_info_bulk_post, name='completed_info_bulk_post'), 
    path('completed-info-bulk-post-view/<post_id>', views.completed_info_bulk_post_view, name='completed_info_bulk_post_view'), 
    path('delete-completed-info-bulk-post/<post_id>', views.delete_completed_info_bulk_post, name='delete_completed_bulk_post'),  
    path('failed-info-bulk-post', views.failed_info_bulk_post, name='failed_info_bulk_post'), 
    path('delete-failed-info-bulk-post/<post_id>', views.delete_failed_info_bulk_post, name='delete_failed_info_bulk_post'),


    path('single-posting', views.single_posting, name='info_single_posting'),  
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  