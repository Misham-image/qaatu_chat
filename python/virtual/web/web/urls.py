"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
<<<<<<< HEAD
from django.contrib import admin
=======
#from django.contrib import admin
>>>>>>> 84c433cfe5ad37f25de32811fd85868ff851981f
from django.urls import path
from django.urls import include



from . import views
urlpatterns = [
  

<<<<<<< HEAD
   path('admin/',admin.site.urls),
=======
   
>>>>>>> 84c433cfe5ad37f25de32811fd85868ff851981f
    

    path('', include('portfolio1.urls')),

    path('', include('display.urls')),
    
    path('', include('daybook.urls')),
<<<<<<< HEAD
    path('', include('medical.urls')),
=======
>>>>>>> 84c433cfe5ad37f25de32811fd85868ff851981f
   path('', views.cache),
]
