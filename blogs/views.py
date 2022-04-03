from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Post



def index(request):
    return  HttpResponse("KHelo melo")

def postlist(request):
    posts=Post.objects.filter(status='published')

    return render(request,'post/list.html',{'posts':posts})

#def postdetail(request,ps,pk):
    #post=get_object_or_404(Post,slug=ps,id=pk)


    #return render(request,'post/detail.html',{'post':ps})









def postdetail(request,post,pk):
    post=Post.published.get(slug=post,id=pk)


    return render(request,'post/detail.html',{'post':post})


