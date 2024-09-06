from django.urls import include, path
from . import views
from .views import logout_view, reset_password,CustomPasswordResetCompleteView, bmi_calculator,select_college_view


urlpatterns=[
  path('', views.login_view , name='login'),
  path('home/', views.home_view , name='home'),
  path('about/', views.about_us , name='about_us'),
  path('signup/', views.signup, name='signup'),
  path('forgot-password/', views.forgot_password, name='forgot-password'),
  path('fitness/', views.fitness_view , name='Fitness'),
  path('health/', views.health_view, name='Health'),
  path('medication/', views.medication, name='medication'),
  path('nutrition/', views.nutrition_view, name='nutrition'),
  path('book_call/', views.book_call, name='book_call'),
  path('success/', views.success, name='success'),
  path('quizzes/', views.quiz_list, name='quiz_list'),
  path('quiz/<int:quiz_id>/', views.take_quiz, name='take_quiz'),
  path('logout/', logout_view, name='logout'),
  path('reset-password/',reset_password, name='reset-password'),
  path('reset/done/', CustomPasswordResetCompleteView.as_view(), name='password_reset_complete'),
  path('bmi/', bmi_calculator, name='bmi_calculator'),
  path('diet/', select_college_view, name='select_college'),
  path('predict/', views.predict_health, name='predict_health'),
  path('healthpredictor/', views.predictor_view, name='predictor_view'),
  path('cardio/', views.cardio_view, name='cardio_view'),
  path('meditation/', views.meditation_view, name='meditation_view'),
  path('weight_training/', views.weight_training_view, name='weight_training_view'),
  path('yoga/', views.yoga_view, name='yoga_view'),
  path('book/', views.book_call, name='book_call'),
  path('chat/', views.chat, name='chat'),
  path('ask_question/', views.ask_question, name="ask_question"),
  path('generate-meal-plan/', views.generate_meal_plan, name='generate_meal_plan'),







  

]