from urllib import request
from django.shortcuts import render,redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import CallBookingForm
from django.shortcuts import render
from django.http import JsonResponse
from django.conf import settings
from django.conf import settings
from .forms import ChatForm
from lib2to3.pgen2 import token
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
import uuid
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponse
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordResetView
from django.shortcuts import render
from .forms import PasswordResetForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_str
from django.utils.crypto import get_random_string
from django.utils.http import urlsafe_base64_decode
from django.shortcuts import redirect
from django.core.mail import EmailMessage
from django.contrib.auth.views import PasswordResetConfirmView
from django.contrib.auth.views import LogoutView
from .forms import CustomPasswordResetForm
from django.contrib.auth.views import PasswordResetCompleteView
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.utils.crypto import get_random_string
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.shortcuts import render
from .forms import SignUpForm
from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseBadRequest
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from .models import Quiz, Question, UserResponse
import os
from django.shortcuts import render
from .forms import MoodForm
from .models import UserInput
from django.shortcuts import render
from .forms import PredictionForm

# Create your views here.
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        remember_me = request.POST.get('remember_me')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            if remember_me:
                request.session.set_expiry(604800)
            else:  
                request.session.set_expiry(0)   
            
            login(request, user)  #updated code to save login data into the session
            request.session['username'] = username  # Store username in session
            messages.success(request, 'Login successful.')
            # Print to nderstand whats happening
            print("User authenticated:", user)
            print("Session username after login:", request.session.get('username'))
            
            return redirect('home/') 
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'base/login.html')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            
            subject = 'Welcome to Our Site'
            message = render_to_string('base/welcome_email.html', {'user': user})
            send_mail(subject, '', settings.EMAIL_HOST_USER, [user.email], html_message=message)
            return redirect('custom_login')  
    else:
        form = SignUpForm()
    return render(request, 'base/sign_UP.html', {'form': form})

def send_welcome_email(user_email, username):
    subject = 'Welcome to Our App!'
    html_message = render_to_string('base/welcome_email.html', {'username': username})
    plain_message = strip_tags(html_message)
    from_email = 'vaibhavpatyal507@gmail.com' 
    send_mail(subject, plain_message, from_email, [user_email], html_message=html_message)

def forgot_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                messages.error(request, 'User with this email does not exist.')
                return redirect('forgot_password')
            
            
            reset_link = request.build_absolute_uri('/') + f'reset-password/'
            send_mail(
                'Password Reset',
                f'Click the link below to reset your password: {reset_link}',
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False,
            )
            messages.success(request, 'Password reset link sent to your email.')
            return redirect('login')
        else:
            messages.error(request, 'Email field is required.')
            return redirect('forgot-password')
    return render(request, 'base/forgot_password.html')


def reset_password(request):
    if request.method == 'POST':
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if password and confirm_password:
            if password != confirm_password:
                messages.error(request, 'Passwords do not match.')
                return redirect('reset_password')
            
            user = User.objects.filter().first()
            if not user:
                messages.error(request, 'Invalid or expired reset token.')
                return redirect('login')

            user.set_password(password)
            user.save()
            messages.success(request, 'Password reset successful. You can now login with your new password.')
            return redirect('login')
        else:
            messages.error(request, 'Password fields are required.')
            return redirect('reset-password')
    return render(request, 'base/reset_password_form.html')



class CustomPasswordResetCompleteView(PasswordResetCompleteView):
    template_name = 'base/password_reset_confirm.html'

def logout_view(request):
    logout(request)
    return redirect('login')


def send_password_reset_email(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            try:
                user = User.objects.get(email=email)
            except User.DoesNotExist:
                pass
            else:
                reset_link = f"http://127.0.0.1:8000/reset-password/{uuid}/{token}/"
                send_mail(
                    'Reset Your Password',
                    f'Click the following link to reset your password: {reset_link}',
                    'vaibhavpatyal507@gmail.com',
                    [email],
                    fail_silently=False,
                )
                return render(request, 'base/password_reset_email_sent.html')
    else:
        form = PasswordResetForm()
    return render(request, 'base/password_reset_form.html', {'form': form})

@login_required
def home_view(request):
    return render(request, 'base/home.html')

@login_required
def fitness_view(request):
    return render(request, 'base/fitness.html')

@login_required
def health_view(request):
    return render(request, 'base/health.html')

@login_required
def medication(request):
    return render(request, 'base/medication.html')

@login_required
def nutrition_view(request):
    return render(request, 'base/nutrition.html')

@login_required
def book_call(request):
    if request.method == 'POST':
        form = CallBookingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = CallBookingForm()
    return render(request, 'base/book_call.html', {'form': form})

def success(request):
    return HttpResponse("Your call has been successfully booked!")
def index(request):
    return render(request, 'base/index.html')



@login_required
def quiz_list(request):
    quizzes = Quiz.objects.all()
    return render(request, 'base/quiz_list.html', {'quizzes': quizzes})

from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Quiz, UserResponse
import random


@login_required
def take_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    
    if request.method == 'POST':
        answers = request.POST.getlist('answers')
        
        # Record user responses
        for question in quiz.questions.all():
            selected_option = request.POST.get(str(question.id))
            UserResponse.objects.create(
                user=request.user,
                question=question,
                selected_option=selected_option
            )
        
        if len(answers) > 0:
            happiness_score = sum(map(int, answers)) / len(answers) * 10
        else:
            happiness_score = random.randint(40, 60)
            message = "Book an Appointment to our Health Expert" if happiness_score < 50 else ""
            
        
        return render(request, 'base/quiz_result.html', {'happiness_score': happiness_score, 'quiz': quiz,'message': message})
    
    else:
        return render(request, 'base/take_quiz.html', {'quiz': quiz})
    
# def mental_health_quiz(request):
#     questions = Question.objects.all()
    
#     if request.method == "POST":
#         answers = request.POST.getlist('answers')
        
#         # Calculate happiness score based on answers
#         happiness_score = sum(map(int, answers)) / len(answers) * 10 
        
#         return JsonResponse({'happiness_score': happiness_score})

#     return render(request, 'base/take_quiz.html', {'questions': questions})

def about_us(request):
    return render(request, 'base/about.html')

def bmi_calculator(request):
    return render(request, 'base/bmi.html')
def fitness(request):
    return render(request, 'base/bmi.html')
def book_call(request):
    return render(request, 'base/appointment.html')

from .forms import CollegeForm
from .models import DietPlan

def select_college_view(request):
    form = CollegeForm()
    diet_plan = None

    if request.method == 'POST':
        form = CollegeForm(request.POST)
        if form.is_valid():
            college = form.cleaned_data['college']
            goal = form.cleaned_data['goal']
            diet_plan = DietPlan.objects.filter(college=college, goal=goal)

    return render(request, 'base/select_college.html', {
        'form': form,
        'diet_plan': diet_plan,
    })
    
# predictions/views.py
import pandas as pd
from django.shortcuts import render
from .forms import HealthInputForm
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

# Pretrained model components (normally you'd load a pre-trained model from disk)
gender_encoder = LabelEncoder()
family_history_encoder = LabelEncoder()
class_encoder = LabelEncoder()

# Mock training data (in real scenario, train and load from disk)
# Similar to the code above, data and encoders are already trained
data = {
    'Age': [45, 30, 60, 50, 35, 42, 55, 28, 65, 38, 52, 48, 70, 33, 57, 44, 29, 62, 54, 36, 68, 40, 47, 25, 58, 37, 66, 41, 32, 59, 53, 34, 64, 43, 49, 27, 61, 39, 67, 46, 19, 22, 21, 23, 18, 24],
    'Gender': ['Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female', 'Male', 'Female'],
    'Diastolic_BP': [85, 75, 90, 80, 70, 88, 92, 68, 95, 78, 82, 84, 96, 72, 87, 83, 74, 91, 86, 76, 93, 79, 85, 70, 89, 77, 94, 81, 73, 88, 90, 71, 92, 80, 84, 69, 88, 75, 91, 82, 65, 68, 70, 69, 66, 72],
    'Family_History': ['Yes', 'No', 'Yes', 'Yes', 'No', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes', 'No', 'Yes', 'No', 'Yes', 'Yes', 'No', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes', 'No', 'Yes', 'No', 'Yes', 'Yes', 'No', 'Yes', 'Yes', 'No', 'Yes', 'Yes', 'Yes', 'No', 'Yes', 'No', 'Yes', 'Yes', 'No', 'No', 'Yes', 'No', 'No', 'Yes'],
    'FBS': [110, 90, 130, 105, 95, 112, 140, 85, 145, 98, 108, 102, 150, 92, 135, 110, 89, 125, 130, 94, 140, 100, 115, 88, 138, 96, 145, 106, 91, 132, 128, 87, 142, 103, 118, 86, 135, 97, 144, 110, 82, 85, 105, 87, 89, 115],
    'Blood_Sugar_Class': ['Prediabetes', 'Normal', 'Diabetes', 'Prediabetes', 'Normal', 'Prediabetes', 'Diabetes', 'Normal', 'Diabetes', 'Normal', 'Prediabetes', 'Prediabetes', 'Diabetes', 'Normal', 'Diabetes', 'Prediabetes', 'Normal', 'Prediabetes', 'Diabetes', 'Normal', 'Diabetes', 'Prediabetes', 'Prediabetes', 'Normal', 'Diabetes', 'Normal', 'Diabetes', 'Prediabetes', 'Normal', 'Diabetes', 'Prediabetes', 'Normal', 'Diabetes', 'Prediabetes', 'Prediabetes', 'Normal', 'Diabetes', 'Normal', 'Diabetes', 'Prediabetes', 'Normal', 'Normal', 'Prediabetes', 'Normal', 'Normal', 'Prediabetes']
}

df = pd.DataFrame(data)

# Encode categorical data
df['Gender'] = gender_encoder.fit_transform(df['Gender'])
df['Family_History'] = family_history_encoder.fit_transform(df['Family_History'])
df['Blood_Sugar_Class'] = class_encoder.fit_transform(df['Blood_Sugar_Class'])

# Features and labels
X = df[['Age', 'Gender', 'Diastolic_BP', 'Family_History']]
y_class = df['Blood_Sugar_Class']
y_fbs = df['FBS']

# Train models
model_class = RandomForestClassifier(random_state=42)
model_class.fit(X, y_class)

model_fbs = RandomForestClassifier(random_state=42)
model_fbs.fit(X, y_fbs)

def predict_health(request):
    if request.method == 'POST':
        form = HealthInputForm(request.POST)
        if form.is_valid():
            age = form.cleaned_data['age']
            gender = gender_encoder.transform([form.cleaned_data['gender']])[0]
            diastolic_bp = form.cleaned_data['diastolic_bp']
            family_history = family_history_encoder.transform([form.cleaned_data['family_history']])[0]

            # Prediction
            new_data = pd.DataFrame({
                'Age': [int(age)],
                'Gender': [gender],
                'Diastolic_BP': [diastolic_bp],
                'Family_History': [family_history]
            })

            class_pred = model_class.predict(new_data)[0]
            fbs_pred = model_fbs.predict(new_data)[0]

            result = {
                'blood_sugar_class': class_encoder.inverse_transform([class_pred])[0],
                'fbs': fbs_pred
            }

            return render(request, 'base/result1.html', {'result': result})

    else:
        form = HealthInputForm()

    return render(request, 'base/input.html', {'form': form})

@login_required
def predictor_view(request):
    return render(request, 'base/health_predictor.html')

def cardio_view(request):
    return render(request, 'base/cardio.html')

def meditation_view(request):
    return render(request, 'base/meditation.html')

def weight_training_view(request):
    return render(request, 'base/weight-training.html')

def yoga_view(request):
    return render(request, 'base/yoga.html')

from .models import Question

# chatbot/views.py
from django.shortcuts import render, reverse
from django.contrib.auth.decorators import login_required
from .models import ChatBot
from django.http import HttpResponseRedirect, JsonResponse
import google.generativeai as genai

# Create your views here.
# add here to your generated API key
genai.configure(api_key="AIzaSyDJwe1QlhnMiB8zUt0cHkAmOdsdqZcr9Sg")


def ask_question(request):
    if request.method == "POST":
        text = request.POST.get("text")
        model = genai.GenerativeModel("gemini-pro")
        chat = model.start_chat()
        response = chat.send_message(text)
        user = request.user
        ChatBot.objects.create(text_input=text, gemini_output=response.text, user=user)
        # Extract necessary data from response
        response_data = {
            "text": response.text,  # Assuming response.text contains the relevant response data
        }
        return JsonResponse({"data": response_data})
    else:
        return HttpResponseRedirect(
            reverse("chat")
        )  # Redirect to chat page for GET requests

def chat(request):
    user = request.user
    chats = ChatBot.objects.filter(user=user)
    return render(request, "base/chat.html", {"chats": chats})

