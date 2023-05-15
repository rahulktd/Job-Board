from django.contrib.auth.forms import UserCreationForm
from django.forms import forms
from django import forms

from Jobs.models import Reg, Job


class SeekerForm(UserCreationForm):
    class Meta:
        model = Reg
        fields = ("email","name","address","mobile",'username','password1','password2')

class EmployerForm(UserCreationForm):
    class Meta:
        model = Reg
        fields = ("name","address","email","mobile",'username','password1','password2')

class JobPostForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title','type','description','location','salary']