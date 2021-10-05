from django.db import models

# Create your models here.
class JobOffer(models.Model):
    company_name = models.CharField(max_length=50)
    company_email = models.EmailField(max_length=255)
    job_title = models.CharField(max_length=50)
    job_description = models.TextField(max_length=500)
    salary = models.FloatField()
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    available = models.BooleanField(default=True)
    created_at = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"{ self.company_name } { self.job_title }"