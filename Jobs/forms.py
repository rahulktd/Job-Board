from django.contrib.auth.forms import UserCreationForm
from django.forms import forms
from django import forms

from Jobs.models import Reg, Job, Feedback, JobApplication


class Dateinput(forms.DateInput):
    input_type = 'date'

class SeekerForm(UserCreationForm):
    birth_date = forms.DateField(widget=Dateinput)
    class Meta:
        model = Reg
        fields = ("email","name","birth_date","address","mobile",'username','password1','password2')

class EmployerForm(UserCreationForm):
    class Meta:
        model = Reg
        fields = ("name","address","email","mobile",'username','password1','password2')

class JobPostForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ('title','type','description','location','salary')

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = ['name', 'email', 'cv']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Reg
        fields = ('username', 'name', 'email', 'birth_date', 'address', 'mobile',)

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ('message',)