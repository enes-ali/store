from django.shortcuts import render
from django.http.response import HttpResponse
from django.views.generic import View
from .models import (
    Category,
    ProductGroup,
    SubCategory,
    ProductType
)



def Home(request):
    categories = Category.objects.all()
    
    return render(request, "home.html", {"categories": categories})