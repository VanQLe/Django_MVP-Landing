from django.db import models

# Create your models here.

class SignUp(models.Model):
	email = models.EmailField()
	full_name = models.CharField(max_length=120, blank=True, null=True) 
	timestamp = models.DateTimeField(auto_now_add = True, auto_now = False) #Timestamp when created 
	update = models.DateTimeField(auto_now_add = False, auto_now = True)# date as when  modified

	def __str__(self):
		return self.email