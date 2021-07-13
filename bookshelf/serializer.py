from django.db import models
from django.db.models import fields
from bookshelf.models import BookShelf
from rest_framework import serializers





class BookShelfSerailizer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only= True)
    user_id = serializers.StringRelatedField(read_only= True)
    book_id = serializers.StringRelatedField(read_only= True)


    def create(self, validate_data):
        return BookShelf.objects.create(**validate_data)




    class Meta:
        model = BookShelf
        fields = '__all__'