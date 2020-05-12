from django.shortcuts import render
from .models import Like,Post
from django.http import HttpResponse


def index(request):
    posts=Post.objects.all()
    return render(request,'app_ajax/index.html',{'posts':posts})

def like(request):
    if request.method=='GET':
        post_id=request.GET['post_id']
        likedpost=Post.objects.get(id=post_id)
        m=Like(post=likedpost)
        m.save()
        return HttpResponse('success')
    else:
        return HttpResponse('unsuccesful')


