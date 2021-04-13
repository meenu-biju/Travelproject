from django.db import models

# Create your models here.

class place(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='picture')
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=False)


class blog(models.Model):
    heading = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now= True)
    desc = models.TextField()
    img= models.ImageField()


class discount(models.Model):
    img=models.ImageField(upload_to='picture')

