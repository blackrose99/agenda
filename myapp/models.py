# models.py
from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    description = models.TextField(blank=True)
    photo = models.ImageField(upload_to='contacts/photos/', blank=True, null=True)

    def __str__(self):
        return self.name
