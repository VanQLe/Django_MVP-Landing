from django.contrib import admin
from .models import SignUp
# Register your models here.
from .forms import SignUpForm



class SignUpAdmin(admin.ModelAdmin):
	list_display = ('__str__', 'timestamp', 'update')
	form = SignUpForm
	# class Meta:
	# 	model = SignUp



admin.site.register(SignUp,SignUpAdmin)