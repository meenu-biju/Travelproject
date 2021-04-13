
from django.http import HttpResponse
from django.shortcuts import render
from . models import place
from .models import blog
from . models import discount



# Create your views here.


def fun(request):
    data = place.objects.all()
    data1 = blog.objects.all()
    data2 = discount.objects.all()
    return render(request,'index.html',{'data': data,'data1':data1,'data2':data2})

#
# def blog(request):
#
#     return render(request, 'index.html', {'data': data})