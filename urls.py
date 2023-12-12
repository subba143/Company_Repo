"""
URL configuration for Company_Proj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from Employee_App import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('list_all/get/', views.Employee_APIview.as_view()),
    path('list_id/get-id/<int:id>/', views.Employee_APIview.as_view()),
    path('create/post/', views.Employee_APIview.as_view()),
    path('update/put/', views.Employee_APIview.as_view()),
    path('update_id/patch/<int:id>/', views.Employee_APIview.as_view()),
    path('delete_id/delete/<int:id>/', views.Employee_APIview.as_view()),

]
