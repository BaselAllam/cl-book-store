from django.db.models import fields
from rest_framework import serializers
from categories.models import Categories



class CategorySerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only = True)
    category_name = serializers.CharField(read_only = True)




    class Meta:
        model = Categories
        fields = '__all__'