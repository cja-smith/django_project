from django.shortcuts import render
from .models import Post

posts = [
	{
		'author': 'Charles',
		'title': 'First blog post',
		'content': 'Testing post',
		'date_posted': '14/09/20'
	},
	{
		'author': 'Charles',
		'title': 'Second blog post',
		'content': 'This is another blog post',
		'date_posted': '14/09/20'
	}

]


def home(request):
	context = {
		'posts': Post.objects.all()
	}
	return render(request, 'blog/home.html',context)

def about(request):
	return render(request, 'blog/about.html', {'title':'About'})