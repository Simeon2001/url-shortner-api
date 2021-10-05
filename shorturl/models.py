from django.db import models

# Create your models here.
class links (models.Model):
    url = models.URLField(blank=False)
    info = models.CharField(max_length=20,blank=True)
    extension = models.CharField(max_length=5,blank=False)

    def __str__(self):
        return self.url