from django.db import models
class Portfolio(models.Model):
    img = models.ImageField(null=True, blank=True, upload_to='static/portfolio')
    title = models.CharField(max_length=20)
    desc = models.CharField(max_length=10)

    def __str__(self):
        return self.title

# Create your models here.
