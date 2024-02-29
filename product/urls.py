from django.urls import path
from product.views import *
from django.contrib.auth.decorators import login_required

app_name = 'product'
urlpatterns = [
    path('',login_required(ProductListView.as_view()), name='product'),
    path('<int:pk>/',ProductDetailView.as_view(), name='product_detail'),
    path('Add/', ProductCreateView.as_view(), name='product_add'),
    path('<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
    path('<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
]

# path('', productsList, name='product'),
# path('<int:id>/',productShow,name='productShow'),
# path('Add/',AddProduct,name='AddProduct'),
# path('Delete/<int:id>/',DeleteProduct,name='DeleteProduct'),
# path('Update/<int:id>/',UpdateProduct,name='UpdateProduct'),

