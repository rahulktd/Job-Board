from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.forms import forms
from django import forms

from Jobs.models import Reg, Job, Feedback, JobApplication


class Dateinput(forms.DateInput):
    input_type = 'date'

class SeekerForm(UserCreationForm):
    birth_date = forms.DateField(widget=Dateinput)
    class Meta:
        model = Reg
        fields = ("email","name","birth_date","qualification","work_experience","mobile","profile_picture",'username','password1','password2')

        def clean_email(self):
            email = self.cleaned_data.get('email')
            if Reg.objects.filter(email=email).exists():
                raise ValidationError(('This email id is already in use.'))
            return email

        def clean_mobile(self):
            mobile = self.cleaned_data.get('mobile')
            if not mobile.isdigit() or len(mobile) != 10:
                raise ValidationError(('Please enter a valid 10 digit mobile number.'))
            return mobile

class EmployerForm(UserCreationForm):
    class Meta:
        model = Reg
        fields = ("name","address","email","mobile","profile_picture",'username','password1','password2')

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
        fields = ("email","name","birth_date","qualification","work_experience","mobile","profile_picture",)

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        fields = ('message',)

class JobApplicationReplyForm(forms.Form):
    reply_message = forms.CharField(widget=forms.Textarea)