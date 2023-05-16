
from django.urls import path

from . import views

urlpatterns = [

    path('', views.index,),
      path('login/',views.login_view,name='login'),
      path('register/',views.registerview.as_view(),name='register'),
    path('create/',views.JournelCreateView.as_view(),name='createjournel'),
    path('list/',views.JournelListView.as_view(),name='listjournel')
]

