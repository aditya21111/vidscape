from django.urls import path,include
from django.urls import include, re_path
from home import views
urlpatterns = [
     path("",views.home,name='home'),
    path("download/",views.download,name='download'),
    path("download_success/",views.download_success,name='download_success'),
    
]