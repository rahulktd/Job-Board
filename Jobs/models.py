from datetime import date

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


# Create your models here.
class Reg(AbstractUser):
    is_recruiter = models.BooleanField(default=False)
    is_seeker = models.BooleanField(default=False)
    email = models.EmailField()
    username = models.CharField(max_length=30,unique=True)
    name = models.CharField(max_length=25, null=True)
    birth_date = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=100, null=True)
    mobile = models.CharField(max_length=20, null=True)
    profile_picture = models.FileField(upload_to='documents/', null=True)

    def __str__(self):
        return str(self.name)

    def age(self):
        if self.birth_date:
            today = date.today()
            return today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))
        return None


class Job(models.Model):
    JOB_CHOICES = [
        ('full_time', 'Full Time'),
        ('part_time', 'Part Time'),
        ('internship', 'Internship')
    ]
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    description = models.TextField()
    location = models.CharField(max_length=255)
    salary = models.CharField(max_length=255)
    posted_by = models.ForeignKey(Reg, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=20, choices=JOB_CHOICES)
    applicant = models.ForeignKey(Reg, on_delete=models.CASCADE, related_name='applied_jobs',null=True,blank=True)

    def __str__(self):
        return self.title

class JobApplication(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    cv = models.FileField()
    job_seeker = models.ForeignKey(Reg, on_delete=models.CASCADE)
    job_post = models.ForeignKey(Job, on_delete=models.CASCADE)
    applied_at = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return f"{self.job_seeker.username} - {self.job_post.title}"
