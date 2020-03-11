from django.contrib import admin
from django.urls import path
from orderManager import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('search_articles', views.search_articles,),
    path('search', views.search,)
   
    
]
