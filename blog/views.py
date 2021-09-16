from django.shortcuts import render, redirect

# Create your views here.
from .models import PostModel
from .forms import PostForm
from blog import views


def update(request,update_id):
	post_form = PostModel.objects.get(id=update_id)
	
	data = {
		'judul'	        : post_form.judul,
		'body'	        : post_form.body,
		'author'		: post_form.author,
		'category'		: post_form.category,
	}
	post_form = PostForm(request.POST or None, initial=data, instance=post_form)

	if request.method == 'POST':
		if post_form.is_valid():
			post_form.save()

		return redirect('blog:list')

	context = {
		"page_title":"Update akun",
		"post_form":post_form,
	}

	return render(request,'blog/create.html',context)

def delete(request,delete_id):
	PostModel.objects.filter(id=delete_id).delete()
	return redirect('blog:list')

def list(request):
	posts	= PostModel.objects.all()

	context = {
		'page_title':'Semua Post',
		'posts':posts,
	}

	return render(request,'blog/list.html',context)

def create(request):
	post_form = PostForm(request.POST or None)

	if request.method == 'POST': # POST request dari browser
		if post_form.is_valid():
			post_form.save()
			return redirect('blog:list')

	context = {
		'page_title':'Create Post',
		'post_form':post_form,
	}

	return render(request,'blog/create.html',context)