from django.db import models
from users.models import CustomUser


class Reviews(models.Model):
    id = models.AutoField(null= False, blank= False, primary_key= True)
    user_id = models.ForeignKey(CustomUser, on_delete= models.RESTRICT)
    rate = models.FloatField(null= False, blank= False, default= 0.0)
    review = models.CharField(null= False, blank= False, default= '', max_length= 225)
    review_date = models.DateField(null= False, blank= False, auto_now= True)




    def __str__(self):
        return 'Book Id: {}, User Id: {}, Rate: {}'.format(self.book_id, self.user_id, self.rate)