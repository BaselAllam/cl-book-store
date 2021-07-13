from django.db import models



class Link(models.Model):
    facebookLink = models.CharField(max_length= 225, blank= False, null= False)
    siteLink = models.CharField(max_length= 225, blank= False, null= False)