from django.contrib import admin
from django.urls import path
from todoapp import views

urlpatterns = [
    path('', views.add, name='add'),
    path('cbvhome/',views.Tasklistview.as_view(),name='cbvhome'),
    path('cbvdetails/<int:pk>/',views.TaskDetailVIew.as_view(),name='cbvdetails'),
    path('cbvupdate/<int:pk>/',views.TaskUpdate.as_view(),name='cbvupdate'),
    path('cbvdelete/<int:pk>/',views.Taskdeleteview.as_view(),name='cbvdelete'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>',views.update,name='update')
    ]
