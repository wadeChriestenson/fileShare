from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('logout/', views.logout, name='logout'),
    path('user.html', views.user_is_true, name='user'),
    path('upload_files.html', views.upload, name='upload'),
    path('download_files.html', views.download, name='download')
]
