
from django.urls import path

from . import views

urlpatterns = [

    path('', views.index,),
<<<<<<< HEAD
      path('login/',views.login_view,name='login'),
      path('register/',views.registerview.as_view(),name='register'),
=======
  
>>>>>>> 84c433cfe5ad37f25de32811fd85868ff851981f
    path('create/',views.JournelCreateView.as_view(),name='createjournel'),
    path('list/',views.JournelListView.as_view(),name='listjournel')
]

