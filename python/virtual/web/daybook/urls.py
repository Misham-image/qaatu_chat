
from django.urls import path

from . import views

urlpatterns = [

    path('', views.index,),
  
    path('create/',views.JournelCreateView.as_view(),name='createjournel'),
    path('list/',views.JournelListView.as_view(),name='listjournel')
]

