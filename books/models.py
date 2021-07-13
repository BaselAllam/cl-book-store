from django.db import models
from categories.models import Categories
from writer.models import Writer


class Books(models.Model):
    id = models.AutoField(null= False, blank= False, primary_key= True)
    book_title = models.CharField(null= False, blank= False, max_length= 50, default= '')
    book_cover = models.ImageField(upload_to= 'books')
    category = models.ForeignKey(Categories, on_delete= models.RESTRICT, related_name= 'category')
    writer = models.ForeignKey(Writer, on_delete= models.RESTRICT, related_name= 'writer')
    book_description = models.CharField(null= False, blank= False, default= '', max_length= 225)
    audio = models.FileField(upload_to= 'books/audio')
    pdf = models.FileField(upload_to= 'books/pdf')
    is_popular = models.BooleanField(null= False, blank= False, default= False)




    def __str__(self):
        return str(self.book_title)