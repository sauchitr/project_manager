from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(default='Project Description')
    deadline = models.DateField(timezone.now())

    def __str__(self):
        return self.name


class Task(models.Model):
    PRIORITY_CHOICES = [    ('High', 'High'),    ('Medium', 'Medium'),    ('Low', 'Low'),]
    priority = models.CharField(max_length=10, choices=PRIORITY_CHOICES, default='Medium')
    project = models.ForeignKey(Project, on_delete=models.CASCADE, default=None)
    name = models.CharField(max_length=255)
    description = models.TextField(default='Task Description')
    due_date = models.DateField(null=True, blank=True)
    assigned_to = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name
    










