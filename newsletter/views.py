from django.shortcuts import render
from .forms import SignUpForm, ContactForm
from django.conf import settings # to use whats in settting.py
from django.core.mail import send_mail

from .models import SignUp


def home(request):
	title = 'Sign Up Now'
	form = SignUpForm(request.POST or None)

	context = {
		"title": title, 
		"form": form

	}

	if form.is_valid():

		instance = form.save(commit = False)
		full_name = form.cleaned_data.get("full_name")# get value to check to do something
		if not full_name:
			full_name = "New full name"
		instance.full_name = full_name
		instance.save()
		# print(instance.email)
		# print(instance.timestamp)
		# print(instance.full_name)
		context = {
			"title":"THANK YOU"
	}

	if request.user.is_authenticated() and request.user.is_staff:
		# print (SignUp.objects.all())
		# for instance in SignUp.objects.all():
		# 	print (instance.full_name)
		queryset = SignUp.objects.all().order_by('-timestamp').filter(full_name__icontains="van")
		# print(SignUp.objects.all().order_by('-timestamp').filter(full_name__icontains="van").count())
		context = {
			"queryset": queryset
		

		}
	return render(request, "home.html", context)


def contact(request):
	title = 'Contact US'
	title_align_center = True
	form = ContactForm(request.POST or None)
	if form.is_valid():
		# for key, value in form.cleaned_data.items():
		# 	print (keßy, value)
		# 	# print (form.cleaned_data.get(key))

		form_email = form.cleaned_data.get("email")
		form_message = form.cleaned_data.get("message")
		form_full_name = form.cleaned_data.get("full_name")
		
		subject= 'Site contact form'
		from_email = settings.EMAIL_HOST_USER 
		to_email = [from_email, 'yourotheremail@email.com']
		contact_message = "%s: %s via %s" %(
		#some_html_message= """ #work with html msg
		##"""
				form_full_name, 
				form_message,
				form_email)

		send_mail(subject, 
				contact_message, 
				from_email, 
				to_email, 
				#html_message = some_html_message, # work with html message
				fail_silently = True)
	context = {
		"form": form,
		"title": title,
		"title_align_center": title_align_center,

	}

	return render(request, "forms.html", context)






