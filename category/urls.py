from django.urls import path
from category.views import *

app_name = 'category'
urlpatterns = [
    path('', categoryList, name='category'),
    path('<int:id>/',categoryShow,name='categoryShow'),
    path('Add/',AddCategory,name='AddCategory'),
    path('Delete/<int:id>/',DeleteCategory,name='DeleteCategory'),
    path('Update/<int:id>/',UpdateCategory,name='UpdateCategory'),
    path('AddCategory', CategoryAddUsingForm, name='CategoryAddUsingForm'),
    path('UpdateCategory/<int:id>', CategoryUpdateView, name='CategoryUpdateView')
]
