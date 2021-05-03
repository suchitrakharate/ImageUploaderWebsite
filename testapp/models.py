from django.db import models

from django.urls import reverse
# Create your models here.
class Image(models.Model):

    photo = models.ImageField(upload_to="myimage")
    caption=models.CharField(max_length=100)

    def get_absolute_url(self):
        return reverse('home')
        

# contact page model
class Contact(models.Model):
    sno= models.AutoField(primary_key=True)
    name= models.CharField(max_length=255)
    phone= models.CharField(max_length=13)
    email= models.CharField(max_length=100)
    content= models.TextField()
    timeStamp=models.DateTimeField(auto_now_add=True, blank=True)


    
    def __str__(self):
        return "Message from " + self.name + ' - ' + self.email