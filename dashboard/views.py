from django.shortcuts import render,redirect
from . models import *
from seller.models import *

def indexhome(request):
    return render(request,'dashboard/homepage.html')
def login(request):
        if request.method=='POST':
            email=request.POST['email']
            password=request.POST['password']
            try:
                 cust=Customer.objects.get(email=email,repass=password)
                 request.session['customer']=cust.id
                 return redirect('dashboard:newhomepage')
            except Customer.DoesNotExist:
                 return render(request,'dashboard/login.html',{'msg':'invalid username or password'})
            # if Customer.objects.filter(email=email,repass=password).exists():
            #      return redirect('dashboard:newhomepage')
            # else:
            #      return render(request,'dashboard/login.html',{'msg':'invaild email'})
            
        return render(request,'dashboard/login.html')


def signup(request):
      if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        number=request.POST['number']
        password=request.POST['repass']
        cust=Customer(name=name,email=email,mob=number,repass=password)
        cust.save()
        return redirect("dashboard:login")
      return render(request,'dashboard/signup.html')
def newhomepage(request):
    return render(request,'dashboard/newhomepage.html')
def aboutus(request):
    return render(request,'dashboard/aboutus.html')

def contactus(request):
        if request.method=='POST':
            name=request.POST['name']
            email=request.POST['email']
            message=request.POST['message']
            cont=Contactus(name=name,email=email,message=message)
            cont.save()
            return redirect('dashboard:homepage')
        return render(request,'dashboard/contactus.html')





def seat(request):
    if 'customer' in request.session:
         
        cat=Category.objects.get(name='seatcover')
        pdts=Product.objects.filter(category=cat)
        return render(request,'dashboard/seat.html',{'product':pdts})
    else:
         return render(request,'dashboard/home.html')
def subwoofer(request):
    if 'customer' in request.session:
        cat=Category.objects.get(name='subwoofer')
        pdts=Product.objects.filter(category=cat)
        return render(request,'dashboard/subwoofer.html',{'product':pdts})
    else:
          return render(request,'dashboard/home.html')
         

def alloys(request):
    if 'customer' in request.session:
        cat=Category.objects.get(name='alloys')
        pdts=Product.objects.filter(category=cat)
        return render(request,'dashboard/wheels.html',{'product':pdts})
    else:
          return render(request,'dashboard/home.html')


def steering(request):
    if 'customer' in request.session:

        cat=Category.objects.get(name='steering')
        pdts=Product.objects.filter(category=cat)
        return render(request,'dashboard/steering.html',{'product':pdts})
    else:
        return render(request,'dashboard/home.html')

def add_to_cart(request,product_id):
     if request.method=='POST':
          product=Product.objects.get(id=product_id)
          cart_item,created=Cart.objects.get_or_create(product=product)
          if not created:
               cart_item.quantity+=1
               cart_item.save()
     return redirect('dashboard:cart')  
  
def cartpage(request):
    cart_items=Cart.objects.all()
    total_price=sum(item.product.price*item.quantity for item in cart_items)
    total_price_per_item=[]
    grand_total=0
    for item in cart_items:
         item_total=item.product.price*item.quantity
         total_price_per_item.append({'item':item,'total':'item_total'})
         grand_total+=item_total
    return render(request,'dashboard/cart.html',{'cart_items':cart_items,'grand_total':grand_total,'total_price':total_price})      


def remove_from_cart(request,product_id):
     product=Product.objects.get(id=product_id)
     cart_item=Cart.objects.get(product=product)
     cart_item.delete()
     return redirect('dashboard:cart')


def logout(request):
     if 'customer' in request.session:
          del request.session['customer']
          return redirect('dashboard:home')
