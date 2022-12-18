from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122,null=True, default='')
    phone = models.CharField(max_length=12,null=True, default='')
    desc = models.TextField(max_length=250,null=True, default='')
    
    def __str__(self):
        return self.name
