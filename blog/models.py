from django.db import models


# Create your models here.
class Blogs(models.Model):
    title =models.CharField(max_length=200)
    pub_date=models.DateField(auto_now_add=False)
    body = models.CharField(max_length=200)
    image = models.ImageField(upload_to="images/")
