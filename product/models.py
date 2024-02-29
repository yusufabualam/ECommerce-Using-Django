from django.db import models
from django.shortcuts import reverse
from category.models import Category

# Create your models here.
class Product(models.Model):
    pname = models.CharField(max_length=100)
    pdetails = models.TextField()
    pimg = models.ImageField(upload_to='product/images', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.pname
    
    @staticmethod
    def get_category_choices():
        return [(category.id, category.cname) for category in Category.objects.all()]

    def __str__(self):
        return  'Name:'+self.name+' email:'+self.email

    @classmethod
    def get_all_products(cls):
        return cls.objects.all()

    @classmethod
    def get_product_by_id(self,id):
        return self.objects.get(id=id)

    def get_trainee_url(self,id):
        return reverse('trainee.details',args=[id])


    def get_trainee_img(self):
        return f'/media/{self.img}'
    

    # category_choices = [(category.id, category.cname) for category in Category.objects.all()]
    # category = models.ForeignKey(Category, on_delete=models.CASCADE, choices=category_choices)