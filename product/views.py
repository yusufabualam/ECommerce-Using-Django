# from django.shortcuts import render,reverse
# from django.http import HttpResponseRedirect
# from .models import *
# from .models import Category

# # Create your views here.
# def productsList(request):
#     print(Product.objects.all())
#     context = {'data':Product.objects.all()}
#     return render(request, 'product/product.html', context)
# #------------------------------------------------------------------------------------------------------
# def productShow(request, id):
#     product = Product.objects.get(id=id)
#     context = {'product': product}
#     return render(request, 'product/show.html', context)
# #------------------------------------------------------------------------------------------------------

# # def AddProduct(request):
# #     if(request.method=='POST'):
# #         pname=request.POST['pname']
# #         pdetails=request.POST['pdetails']
# #         pimg = request.FILES['pimg']
# #         Product.objects.create(pname=pname,pdetails=pdetails,pimg=pimg)
# #         return HttpResponseRedirect(reverse('product:product'))
# #     return render(request,'product/insert.html')

# def AddProduct(request):
#     if request.method == 'POST':
#         pname = request.POST['pname']
#         pdetails = request.POST['pdetails']
#         pimg = request.FILES['pimg']
#         category_id = request.POST['category']  
#         category = Category.objects.get(id=category_id)

#         Product.objects.create(pname=pname, pdetails=pdetails, pimg=pimg, category=category)
#         return HttpResponseRedirect(reverse('product:product'))
    
#     categories = Category.objects.all()

#     context = {'categories': categories}
#     return render(request, 'product/insert.html', context)
# # ------------------------------------------------------------------------------------------------------------
# def DeleteProduct(request,id):
#     Product.objects.filter(id=id).delete()
#     return HttpResponseRedirect(reverse('product:product'))

# def UpdateProduct(request,id):
#     context={}
#     if(request.method=='POST'):
#         print(request.POST)
#         Product.objects.filter(id=id).update(
#             pname=request.POST['pname'],
#             pdetails=request.POST['pdetails'],
#             pimg=request.POST['pimg'],
#         )
#         return HttpResponseRedirect(reverse('category:category'))
#     product=Product.objects.get(id=id)
#     context['product']=product
#     return render(request,'product/update.html',context)
# #------------------------------------------------------------------------------------------------------
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .models import Product
from .models import Category
from django.contrib.auth.decorators import login_required

class ProductListView(ListView):
    model = Product
    template_name = 'product/product.html'
    context_object_name = 'data'

#------------------------------------------------------------------------------------------------------

class ProductDetailView(DetailView):
    model = Product
    template_name = 'product/show.html'
    context_object_name = 'product' 

#------------------------------------------------------------------------------------------------------

class ProductCreateView(CreateView):
    model = Product
    template_name = 'product/insert.html'
    fields = ['pname', 'pdetails', 'pimg', 'category']

    def form_valid(self, form):
        category_id = self.request.POST.get('category')
        category = Category.objects.get(id=category_id)
        form.instance.category = category
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all() 
        return context
    
    def get_success_url(self):
        return reverse_lazy('product:product')
    
#------------------------------------------------------------------------------------------------------

class ProductDeleteView(DeleteView):
    model = Product
    template_name = 'product/delete.html'
    success_url = reverse_lazy('product:product') 

#------------------------------------------------------------------------------------------------------

class ProductUpdateView(UpdateView):
    model = Product
    template_name = 'product/update.html'
    fields = ['pname', 'pdetails', 'pimg', 'category']
    success_url = reverse_lazy('product:product') 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context

    def form_valid(self, form):
        print("Form is valid. Updating product...")
        if form.is_valid():
            print("Form is valid. Saving form data...")
            form.save()
        else:
            print("Form is not valid. Errors:", form.errors)
        return super().form_valid(form)

