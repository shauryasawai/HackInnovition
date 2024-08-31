from django.contrib import admin
from .models import Quiz, Question, UserResponse
from .models import College, FoodItem, Goal, DietPlan

# Register your models here
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(UserResponse)
admin.site.register(College)
admin.site.register(FoodItem)
admin.site.register(Goal)
admin.site.register(DietPlan)

