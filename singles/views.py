from django.shortcuts import render

APP_NAME='singles'

def home(request):
	return render(request, 'index.html')

def about(request):
	return render(request, 'singles/about.html')

def contact(request):
	return render(request, 'singles/contact.html')