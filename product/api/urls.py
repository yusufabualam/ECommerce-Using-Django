from django.urls import path
from . import views

urlpatterns = [
    path('getbyid/<id>',views.getbyid, name='getbyid'),
    path('deletebyid/<id>',views.deletebyid, name='deletebyid'),
    path('all/',views.getall, name='getall'),
     path('add/',views.add, name='add'),
     path('update/<id>',views.updatebyid, name='updatebyid'),
]