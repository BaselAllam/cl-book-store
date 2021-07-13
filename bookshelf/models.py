from django.db import models
from books.models import Books
from users.models import CustomUser


class BookShelf(models.Model):
    id = models.AutoField(null= False, blank= False, primary_key= True)
    user_id = models.ForeignKey(CustomUser, on_delete= models.RESTRICT)
    book_id = models.ForeignKey(Books, on_delete= models.RESTRICT)




    def __str__(self):
        return 'User: {}, Book: {}'.format(self.user_id, self.book_id)