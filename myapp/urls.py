from django import views
from django.urls import  path
from . import views 
urlpatterns=[
    path('',views.index,name='index'),
    path('Audio',views.Audio,name='Audio'),
    path('content',views.content,name='content')
]

