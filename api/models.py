from django.db import models

class Test(models.Model):
    image = models.ImageField(upload_to='images/', null=True)
    title = models.CharField(max_length=100, null=True)
    subtitle = models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.title[:10]