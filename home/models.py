from sqlite3 import Timestamp
from django.db import models

# Create your models here.


class Contact(models.Model):
    sno = models.AutoField(primary_key=True)
    name = models.CharField(max_length=225)
    phone = models.CharField(max_length=13)
    email = models.CharField(max_length=100)
    content = models.TextField()
    timeStamp = models.DateTimeField(auto_now_add=True, blank=True)
    
    def __str__(self):                                                     # To display the user name who trying to contact you
        return 'Message from ' + self.name + ' - ' + self.email
