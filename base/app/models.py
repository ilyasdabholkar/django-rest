from django.db import models

# Create your models here.

class Members(models.Model):
    name = models.CharField(null=False,max_length=100)
    email = models.TextField(null=False)
    level = models.TextField(null=False)

    def __str__(self):
        return self.name