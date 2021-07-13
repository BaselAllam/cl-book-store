from django.db import models




class Categories(models.Model):
    id = models.AutoField(null= False, blank= False, primary_key= True)
    category_name = models.CharField(null= False, blank= False, default= '', max_length= 50)




    def __str__(self):
        return str(self.category_name)