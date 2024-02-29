from rest_framework import serializers
from product.models import Product
from category.models import Category
from rest_framework.validators import UniqueValidator

class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    pname = serializers.CharField(validators=[UniqueValidator(queryset=Product.objects.all())], max_length=50)
    pdetails = serializers.CharField()
    pimg = serializers.ImageField(allow_empty_file=True)
    category_id = serializers.IntegerField()

    def create(self, validated_data):
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.pname = validated_data.get('pname', instance.pname)
        instance.pdetails = validated_data.get('pdetails', instance.pdetails)
        instance.pimg = validated_data.get('pimg', instance.pimg)
        instance.category_id = validated_data.get('category_id', instance.category_id)
        instance.save()
        return instance
    
    class Meta:
        model = Product
        fields = '__all__'




