from django.shortcuts import render
from django.http import HttpResponse
from  django.shortcuts import render
from .models import category
from .models import products
# Create your views here.

def dashboard(request):
    category.objects.all()
    info = category.objects.filter()
    print(info)
    return render(request, 'dashboard/dashboard.html', {'data': info})

def contact_us(request):
    return  render(request, 'contact_us/contact_us.html')

def cart(request):
    return render(request, 'cart/cart.html')


def get_product(request, CategoryName):
    category_name = CategoryName
    cat_id = category.objects.get(CategoryName=category_name)
    pro_info = products.objects.filter(categoryId_id=cat_id.id)
    return render(request, 'products/get_product.html', {'pro_info': pro_info, 'category_name':category_name})

def pro_desc(request):
    return render(request, 'products/pro_desc.html')

