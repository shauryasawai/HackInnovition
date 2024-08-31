from django import forms
from .models import CallBooking
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.forms import UserCreationForm
from .models import College, Goal

class CallBookingForm(forms.ModelForm):
    class Meta:
        model = CallBooking
        fields = ['name', 'phone', 'email', 'date']
        
class ChatForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea, label='Your Message')

class PredictionForm(forms.Form):
    bmi = forms.FloatField(label='BMI')
    blood_pressure = forms.FloatField(label='Blood Pressure')

class MoodForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea, label='Enter your text')
class SignUpForm(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].help_text = None

    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    
    name = forms.CharField(label='name', max_length=100)
    
    phone_no = forms.CharField(max_length=20)

    email = forms.EmailField( label='Email', required=True)
    
    address = forms.CharField()


    class Meta:
        model = User
        fields = ['username',     'email', 
                  
                  'password1', 'password2',  'name',  'phone_no', 'address' ]
        
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("This email address is already in use.")
        return email



class CustomPasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class PasswordResetForm(forms.Form):
    email = forms.EmailField()

class BMICalculatorForm(forms.Form):
    height = forms.FloatField(label='Height (cm)', min_value=0)
    weight = forms.FloatField(label='Weight (kg)', min_value=0)

class CollegeForm(forms.Form):
    college = forms.ModelChoiceField(queryset=College.objects.all(), label="Select Your College")
    goal = forms.ModelChoiceField(queryset=Goal.objects.all(), label="Select Your Goal")