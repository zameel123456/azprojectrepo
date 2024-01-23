from django.shortcuts import render,redirect
from.models import *


# Create your views here.


def seller_login(request):
    if request.method=='POST':
        email=request.POST['email']
        password=request.POST['password']
        if Seller.objects.filter(email=email,password=password):
            return redirect('seller:sdashboard')

    return render(request,'seller/login.html')
def seller_dashboard(request):
    pdt=Product.objects.all()
    return render(request,'seller/sdashboard.html',{'pdt':pdt})
def addpdt(request):
    categories=Category.objects.all()
    if request.method=='POST':
        name=request.POST['name']
        description=request.POST['description']
        price=request.POST['price']
        image=request.FILES['image']
        category_id=request.POST.get('category')
       
       
        category=Category.objects.get(pk=category_id)
        product=Product(name=name,description=description,price=price,image=image,category=category)
        product.save()
    return render(request,'seller/addpdt.html',{'categories':categories})
def pdt_update(request,pid):
    categories=Category.objects.all()
    product=Product.objects.get(id=pid)
    if request.method=='POST':
        name=request.POST['name']
        description=request.POST['description']
        price=request.POST['price']
        category_id=request.POST.get('category')
        category=Category.objects.get(pk=category_id)
        product.name=name
        product.description=description
        product.price=price
        if 'image' in request.FILES:
            image = request.FILES['image']
            product.image = image
        else:
            image = product.image if product.image else None
        product.category=category
        product.save()
        return redirect('seller:sdashboard')
        
    return render(request,'seller/updatepdt.html',{'product':product,'categories':categories})
def Update(request):
    return render(request,'dashboard/update.html')
def pdt_delete(request,pid):
    Product.objects.get(id=pid).delete()
    return redirect('seller:sdashboard')