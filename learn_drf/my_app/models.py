from django.db import models

# Create your models here.

class Books(models.Model):
    name = models.CharField(max_length=120)
    author = models.CharField(max_length=130)
    author_email = models.EmailField()

    def __str__(self):
        return self.name
    

class ModelA(models.Model):
   name = models.CharField(max_length=120)
 
class ModelB(models.Model):
   a = models.ForeignKey(ModelA, on_delete=models.CASCADE)