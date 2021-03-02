from django.shortcuts import render
from . import models
# Creyour views here.
def articles_list(request):
    articles=models.Articles.objects.all().order_by('date')

    return render(request,'articles/articleslist.html',{'articles':articles})
