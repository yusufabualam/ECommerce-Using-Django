from django.db import models

# Create your models here.
class Category(models.Model):
    cname = models.CharField(max_length=100)

    @classmethod
    def create(cls, name):
        category = cls(cname=name)
        category.save()
        return category