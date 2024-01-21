from django.contrib import admin
from .models import UserProfile
from .models import Diary

admin.site.register(UserProfile)

admin.site.register(Diary)
# Register your models here.
