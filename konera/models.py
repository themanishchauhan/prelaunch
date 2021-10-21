from django.db import models

# Create your models here.

class Email(models.Model):
    name = models.TextField(max_length=64)
    email = models.EmailField(max_length=244)
    def __str__(self):
        return self.name
