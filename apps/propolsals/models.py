from django.db import models

# Create your models here.

class Proposal(models.Model):
    proposed_by = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=12)
    email = models.EmailField(max_length=255)
    file = models.FileField(upload_to='proposals/')
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title