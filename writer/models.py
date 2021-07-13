from django.db import models



class Writer(models.Model):
    id = models.AutoField(null= False, blank= False, primary_key= True)
    writer_name = models.CharField(null= False, blank= False, default= '', max_length= 50)



    def __str__(self):
        return str(self.writer_name)