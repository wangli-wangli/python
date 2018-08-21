from django.shortcuts import render
from django.http import HttpResponse
from . import models
#响应函数
def index(request):#函数名，目录页面
    articles=models.Article.objects.all()#得到全部的数据库中的article
    return render(request, 'blog/index.html', {'articles': articles})#跳转到目录页面，跳转页面的参数

def article_page(request,article_id):#查看文章
    article=models.Article.objects.get(pk=article_id)#得到数据库中id为article_id的article数据
    return render(request,'blog/article_page.html',{'article':article})
def edit_page(request,article_id):#编辑文章
    if str(article_id)=='0':#如果article_id为0，则为新文章
        return render(request,'blog/edit_page.html')#跳转到文章编辑页面
    article=models.Article.objects.get(pk=article_id)#否则article为相应id的文章
    return render(request, 'blog/edit_page.html', {'article': article})#编辑该文章

def edit_action(request):#编辑文章提交函数
    title=request.POST.get('title','TITLE')#接受action的参数
    content=request.POST.get('content','CONTENT')
    article_id=request.POST.get('article_id','0')#得到编辑文章的id
    if article_id=='0':#如果i编辑的文章id为0
        models.Article.objects.create(title=title,content=content)#在数据库中新增article数据
        articles = models.Article.objects.all()#得到全部的数据库中的article
        return render(request, 'blog/index.html', {'articles': articles})#跳转到目录页面，跳转页面的参数
    #获得对象
    article=models.Article.objects.get(pk=article_id)
    #修改数据库数据
    article.title=title
    article.content=content
    article.save()
    #跳转到文章页面
    return render(request, 'blog/article_page.html', {'article': article})


