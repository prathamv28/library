from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.
class Librarian(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE , primary_key=True)
    def __str__(self):
        return self.user.username

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=30)
    publisher = models.CharField(max_length=50)
    datetime= models.DateTimeField(default=timezone.now)
    count = models.IntegerField()
    issued_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title + '-' + self.author

class Customer(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE , primary_key=True)
    issued_book= models.ForeignKey(Book,default=None,null=True)
    def __str__(self):
        return self.user.username

