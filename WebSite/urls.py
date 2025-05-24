"""
URL configuration for project01 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from . import views
app_name = 'WebSite'
urlpatterns = [
    #path('admin/', admin.site.urls),
    path('home/', views.home, name='home'),
    path('character_list/', views.character_list, name='character_list'),
    path('get_anime/', views.get_anime, name='get_anime'),
    path('get_manga/', views.get_manga, name='get_manga'),
    path("objects_array/", views.objects_arrays, name="objects_array"),
    path('affordable-artworks/<str:artworks>/<int:budget>/', views.get_affordable_artworks, name='affordable_artworks'),
    path('shop/', views.get_shop, name='get_shop'),
    path('order/', views.get_order, name='get_order'),
    path('hse_studies/', views.hse_studies_main, name='hse_studies_main'),
    path('hse_studies/my-profile/', views.my_profile, name='my_profile'),
    path('hse_studies/educational-program/', views.educational_program, name='educational_program'),
    path('hse_studies/program-management/', views.program_management, name='program_management'),
    path('hse_studies/classmates/', views.classmates, name='classmates'),
]