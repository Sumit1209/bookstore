from django.db import models

# Create your models here.
class Contact(models.Model):
    name= models.CharField(max_length=122)
    email= models.CharField(max_length=122)
    phone= models.CharField(max_length=122)
    desc= models.TextField()
    date= models.DateField()

    def __str__(self):
        return self.name


class Detail(models.Model):
    subject=models.CharField(max_length=120)
    writer= models.CharField(max_length=120)
    publication=models.CharField(max_length=120)
    about=models.CharField(max_length=120)
    file_1=models.FileField(upload_to="Hello/",max_length=1000,null=True,default=None)
    buttona=models.FileField(upload_to="Hello/",max_length=1000,null=True,default=None)

    def __str__(self):
        return self.subject



   

