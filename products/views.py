from django.shortcuts import render
from .models import Products
from django.shortcuts import redirect, HttpResponseRedirect
from django.contrib.auth.models import User

# Create your views here.

def home(request):
	pictures = Products.objects.filter(type="1")[:4]
	logo = Products.objects.filter(type="2")[:4]
	poster = Products.objects.filter(type="3")[:4]
	videos = Products.objects.filter(type="4")[:4]

	context = {
		'pictures':pictures,
		'logo': logo,
		'poster':poster,
		'videos':videos,
	}
	return render(request,'index.html',context)

def picture(request):
	pictures = Products.objects.filter(type="1")

	path = request.get_full_path()
	context = {
		'path':path,
		'pictures':pictures,
	}
	return render(request,'picture.html',context)

def logo(request):
	logo = Products.objects.filter(type="2")

	context = {
		'logo':logo,
	}
	return render(request,'logo.html',context)

def poster(request):
	poster = Products.objects.filter(type="3")

	context = {
		'poster':poster,
	}
	return render(request,'poster.html',context)

def videos(request):
	videos = Products.objects.filter(type="3")

	context = {
		'videos':videos,
	}
	return render(request,'video.html',context)