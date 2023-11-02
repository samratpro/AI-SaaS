# URL Mapping in App URL file----------------------
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('profile', views.profile, name='profile'),   
    path('login/', views.login, name='login'),   
    path('logout', views.logout, name='logout'),   
    path('register', views.register, name='register'),   
    path('activate/<str:activation_code>/', views.activate_account, name='activate_account'),
    path('forget', views.forget, name='forget'),   
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)