from django.shortcuts import render,reverse, redirect
from django.http import HttpResponseRedirect
from .models import Category
from .forms import *

# Create your views here.
def categoryList(request):
    print(Category.objects.all())
    context = {'data':Category.objects.all()}
    return render(request, 'category/category.html', context)

def categoryShow(request, id):
    category = Category.objects.get(id=id)
    context = {'category': category}
    return render(request, 'category/show.html', context)

def AddCategory(request):
    if(request.method=='POST'):
        cname=request.POST['cname']
        Category.objects.create(cname=cname)
        return HttpResponseRedirect(reverse('category:category'))
    return render(request,'category/insert.html')

def DeleteCategory(request,id):
    Category.objects.filter(id=id).delete()
    return HttpResponseRedirect(reverse('category:category'))

def UpdateCategory(request,id):
    context={}
    if(request.method=='POST'):
        print(request.POST)
        Category.objects.filter(id=id).update(
            cname=request.POST['cname'],
        )
        return HttpResponseRedirect(reverse('category:category'))
    category=Category.objects.get(id=id)
    context['category']=category
    return render(request,'category/update.html',context)

#---------------------------------------------------------------------------------------------------------
def CategoryAddUsingForm(request):
    form = CategoryAddForm()
    context = {'form': form, 'msg': ''}
    if request.method == 'POST':
        form = CategoryAddForm(request.POST)
        if form.is_valid():
            cname = form.cleaned_data['cname']
            Category.objects.create(cname=cname)
            return HttpResponseRedirect(reverse('category:category'))
        else:
            context['msg'] = 'A category with this name already exists.'
    return render(request, 'category/Add.html', context)

# ------------------------------------------------------------------------------------------------------------

def CategoryUpdateView(request, id):
    context = {}
    try:
        category = Category.objects.get(id=id)
    except Category.DoesNotExist:
        
        return redirect(reverse('category:category'))

    if request.method == 'POST':
        form = CategoryUpdateForm(request.POST, instance=category)
        if form.is_valid():
            cname = form.cleaned_data['cname']
            if Category.objects.filter(cname=cname).exclude(id=id).exists():
                context['msg'] = 'A category with this name already exists.'
            else:
                category.cname = cname
                category.save()
                return redirect(reverse('category:category'))
    else:
        form = CategoryUpdateForm(instance=category)  

    context['form'] = form
    context['category'] = category
    return render(request, 'category/UpdateForm.html', context)
