from django.contrib import admin
#Calling models from models.py file to see in admin interface
from .models import Question, Choice
# Register your models here.
admin.site.register(Question)
admin.site.register(Choice)
