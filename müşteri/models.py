from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, null=True)
    slug = models.SlugField(unique=True, null=True, max_length=60)
    
    def __str__(self):
        return self.name

class Client(models.Model):

    name = models.CharField(max_length=100 )
    category = models.ForeignKey(Category, null=True, on_delete=models.DO_NOTHING)
    tc =  models.IntegerField()
    plaka = models.CharField(max_length=11)
    date = models.DateField()
    telefon =models.IntegerField()
    piece =models.IntegerField()
    tents =models.IntegerField()
    depozito =models.CharField(max_length=5)
    tip =models.CharField(max_length=25)


    def __str__(self):
        return self.name
