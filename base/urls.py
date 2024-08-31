from django.urls import include, path
from . import views
from .views import logout_view, reset_password,CustomPasswordResetCompleteView, bmi_calculator,select_college_view


urlpatterns=[
  path('', views.login_view , name='login'),
  path('home/', views.home_view , name='login'),
  path('about/', views.about_us , name='login'),
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




  

]