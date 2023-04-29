from django import forms
from .models import Project, Task
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProjectForm(forms.ModelForm):

    deadline = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Project
        fields = ['name', 'description', 'deadline']

class TaskForm(forms.ModelForm):
    # PRIORITY_CHOICES = [
    #     ('low', 'Low'),
    #     ('medium', 'Medium'),
    #     ('high', 'High'),
    # ]

    due_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    # priority = forms.ChoiceField(choices=PRIORITY_CHOICES)

    PRIORITY_CHOICES = [    ('H', 'High'),    ('M', 'Medium'),    ('L', 'Low'),]

    priority = forms.ChoiceField(choices=PRIORITY_CHOICES, widget=forms.RadioSelect)


    class Meta:
        model = Task
        fields = ['name', 'description', 'due_date', 'priority', 'assigned_to']




class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']