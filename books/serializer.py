from rest_framework import serializers
from books.models import Books



class BooksSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only = True)
    book_title = serializers.CharField(read_only = True)
    book_cover = serializers.ImageField(read_only = True)
    category = serializers.StringRelatedField()
    writer = serializers.StringRelatedField()
    book_description = serializers.CharField(read_only = True)
    audio = serializers.FileField(read_only = True)
    pdf = serializers.FileField(read_only = True)
    is_popular = serializers.BooleanField(read_only = True)





    class Meta:
        model = Books
        fields = '__all__'