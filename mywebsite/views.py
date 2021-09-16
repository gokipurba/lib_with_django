from django.shortcuts import render#untuk mengambil metode yang ada di templates

def index(request):
	context = {
		'page_title':'Home',
	}

	return render(request, 'index.html',context)

def about(request):
	return render(request, "about.html")

def coba (request):
	return render(request, "coba.html")