from django import forms
from .models import Category
from django.core.exceptions import ValidationError

class CategoryAddForm(forms.Form):
    cname=forms.CharField(label='Name ',max_length=50)

    def clean_cname(self):
        cname = self.cleaned_data['cname']
        if Category.objects.filter(cname=cname).exists():
            raise ValidationError('A category with this name already exists.')
        return cname

class CategoryUpdateForm(forms.Form):
    cname = forms.CharField(label='Name', max_length=50)

    def __init__(self, *args, **kwargs):
        self.instance = kwargs.pop('instance')
        super(CategoryUpdateForm, self).__init__(*args, **kwargs)
        self.fields['cname'].initial = self.instance.cname

    def clean_cname(self):
        cname = self.cleaned_data['cname']
        if cname == self.instance.cname:
            return cname
        if Category.objects.filter(cname=cname).exists():
            raise forms.ValidationError('A category with this name already exists.')
        return cname