from django.db import models


# Create your models here.
class Blogs(models.Model):
    title =models.CharField(max_length=500)
    pub_date=models.DateField(auto_now_add=False)
    body = models.CharField(max_length=200)
    image = models.ImageField(upload_to="images/")

    def summary(self):
        return self.body[:100]
    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')

    def __str__(self):
        return self.title
