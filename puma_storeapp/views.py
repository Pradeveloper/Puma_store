from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.db import IntegrityError
from puma_storeapp.models import Product, Store, Order
from django.db.models import Q
import random 
import razorpay
# Create your views here.
def home(request):
    userid = request.user.id
    return render(request, 'index.html')
def Brands(request):
    context = {}
    p = Product.objects.filter(is_active=True)
    context['Products'] = p
    print(p)
    return render(request, 'Brands.html',context)
def pdetails(request, pid):
    # Your view logic here
    context = {}
    # Use filter to retrieve a queryset
    products = Product.objects.filter(id=pid)
    context['Products'] = products
    return render(request, 'pdetails.html', context)
def viewcart(request):
    c=Store.objects.filter(Uid=request.user.id)
    print(c)
    print(c[0].Pid)
    print(c[0].Uid)
    print(c[0].created_at)
    print(c[0].Pid.name)
    context={}
    context['data']=c
    s=0
    for x in c:
        #print(x)
        #print(x.pid.price)
        s=s+x.Pid.price* x.qty
        print(s)
    context['total']=s
    return render(request, 'viewcart.html', context)
    
def register(request):
    if request.method == "POST":
        uname = request.POST.get('uname')
        upass = request.POST.get('upass')
        ucpass = request.POST.get('ucpass')

        context = {}
        if uname == "" or upass == "" or ucpass == "":
            context['errmsg'] = "Fields cannot be empty"
            return render(request, "register.html", context)
        elif upass != ucpass:
            context['errmsg'] = "Passwords did not match"
            return render(request, "register.html", context)
        else:
            try:
                u = User.objects.create(username=uname, email=uname)
                u.set_password(upass)
                u.save()

                context['success'] = "User registered successfully"
                return render(request, "register.html", context)
            except IntegrityError:
                context['errmsg'] = "User already exists! Try login."
                return render(request, "register.html", context)
    else:
        return render(request, 'register.html')
def ulogin(request):
    if request.method == "POST":
        uname = request.POST['uname']
        upass = request.POST['upass']
        context = {}
        if uname == "" or upass == "":
            context['errmsg'] = "Fields cannot be empty."
            return render(request, 'login.html', context)
        else:
            user = authenticate(username=uname, password=upass)
            if user is not None:
                # If authentication is successful, log the user in
                login(request, user)
                return redirect('/home')
            else:
                context['errmsg'] = "Invalid Username/password."
                return render(request, 'login.html', context)
    else:
        return render(request, 'login.html')
    
def logout_view(request):
    logout(request)
    return redirect('/home')
def catfilter(request, cv):
    q1=Q(is_active=True)
    q2=Q(cat=cv)
    p=Product.objects.filter(q1 & q2)
    print(p)
    context={}
    context['Products'] = p
    return render(request, 'Brands.html', context)
def sort(request, sv):
    if sv == '0':
        col = 'price'
    else:
        col = '-price'
    
    p = Product.objects.filter(is_active=True).order_by(col) 
    context = {}
    context['Products'] = p
    return render(request, 'Brands.html', context)
def range(request):
    min_value = request.GET.get('min')
    max_value = request.GET.get('max')

    q1 = Q(price__gte=min_value)
    q2 = Q(price__lte=max_value)
    q3 = Q(is_active=True)

    p = Product.objects.filter(q1 & q2 & q3)

    context = {}
    context['Products'] = p
    return render(request, 'Brands.html', context)

def addtocart(request, pid):
    if request.user.is_authenticated:
        userid = request.user.id
        u = User.objects.filter(id=userid)
        print(u)

        p = Product.objects.filter(id=pid)
        print(p)

        q1 = Q(Uid=u[0])
        q2 = Q(Pid=p[0])

        c = Store.objects.filter(q1 & q2)
        print(c)
        context = {}
        n = len(c)
        if n == 1:
            context['errmsg'] = "Product already exists in cart!!"
            context['Products'] = p
            return render(request, 'pdetails.html', context)
        else:
            c = Store.objects.create(Uid=u[0], Pid=p[0])
            c.save()
            context['success'] = "Product added to cart!!"
            context['Products'] = p
            return render(request, 'pdetails.html', context)
    else:
        return redirect('/login')
def remove(request, cid):
    c=Store.objects.filter(id=cid)
    c.delete()
    return redirect('/viewcart')
def updateqty(request,qv,cid):
    c=Store.objects.filter(id=cid)
    print(c[0])
    print(c[0].qty)
    if qv=='1':
        t=c[0].qty+1
        c.update(qty=t)
    else:
        t=c[0].qty-1
        c.update(qty=t)
    return redirect('/viewcart')
def placeorder(request):
    userid = request.user.id

    items_in_cart = Store.objects.filter(Uid=userid)

    oid = random.randrange(1000, 9999)

    for item in items_in_cart:
        order = Order.objects.create(order_id=oid, Pid=item.Pid, Uid=item.Uid, qty=item.qty)
        order.save()
        item.delete()


    orders = Order.objects.filter(Uid=request.user.id)

  
    total = sum(order.Pid.price * order.qty for order in orders)
    num_items = len(orders)

    context = {
        'data': orders,
        'total': total,
        'items': num_items
    }
    return render(request, 'placeorder.html', context)

def makepayment(request):
    orders=Order.objects.filter(Uid=request.user.id)
    s=0
    np=len(orders)
    for x in orders:
        s=s+x.Pid.price * x.qty
        oid=x.order_id

    client = razorpay.Client(auth=("rzp_test_D59nTnf05neQHK", "1b48k5P602ToDzFSIbZX4tLF"))
    data = { "amount":s*100, "currency": "INR", "receipt": oid }
    payment = client.order.create(data=data)
    context={}
    context['data']=payment
    #return HttpResponse("In payment pg!!")
    return render(request,'pay.html',context)
    