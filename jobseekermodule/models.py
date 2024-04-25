from django.db import models

# Create your models here.
# models.py
from django.db import models


class JobApplication(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    job_details = models.CharField(max_length=200)
    resume = models.FileField(upload_to='resumes/', null=True, blank=True)
    cover_letter = models.TextField()

    def __str__(self):
        return self.name
