# URL Mapping in App URL file----------------------
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('bulk-posting', views.bulk_posting, name='info_bulk_posting'),  
    path('completed-bulk-posts', views.completed_info_bulk_post, name='completed_info_bulk_post'), 
    path('completed-bulk-single-view/<post_id>', views.completed_info_bulk_single_view, name='completed_info_bulk_single_view'), 
    path('delete-completed-bulk-post/<post_id>', views.delete_completed_info_bulk_post, name='delete_completed_info_bulk_post'),  
    path('failed-bulk-posts', views.failed_info_bulk_post, name='failed_info_bulk_post'), 
    path('delete-failed-bulk-post/<post_id>', views.delete_failed_info_bulk_post, name='delete_failed_info_bulk_post'),


    path('single-posting', views.single_posting, name='info_single_posting'),  
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  