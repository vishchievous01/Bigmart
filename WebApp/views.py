from django.shortcuts import render, redirect
from Backend.models import ProductDb, BigmartDb
from WebApp.models import ContactDb, RegisterDB, CartDb, subscribeDB, OrderDB
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
import razorpay


# Create your views here.

def homepage(request):
    cat = BigmartDb.objects.all()
    first_cat = cat.first()
    return render(request, "Home.html", {'cat': cat, 'first_cat': first_cat})


def aboutpage(req):
    cat = BigmartDb.objects.all()
    first_cat = cat.first()
    return render(req, "About.html", {'cat': cat, 'first_cat': first_cat})


def contactpage(req):
    cat = BigmartDb.objects.all()
    first_cat = cat.first()
    return render(req, "Contact.html", {'cat': cat, 'first_cat': first_cat})


def ourproducts_cat(req):
    cat = BigmartDb.objects.all()
    first_cat = cat.first()
    return render(req, "Our_products.html", {'cat': cat, 'first_cat': first_cat})


def ourproducts(req):
    pdata = ProductDb.objects.all()
    return render(req, "Our_products.html", {'pdata': pdata})


def save_contact(request):
    if request.method == "POST":
        nm = request.POST.get('name')
        em = request.POST.get('email')
        ph = request.POST.get('phone')
        sub = request.POST.get('subject')
        msg = request.POST.get('message')
        obj = ContactDb(Name=nm, Email=em, Phone=ph, Subject=sub, Message=msg)
        obj.save()
        return redirect(contactpage)


def filtered_products(req, cat_name):
    data = ProductDb.objects.filter(Category=cat_name)
    return render(req, "Products_filtered.html", {'data': data})


def categories_page(req):
    return render(req, "Categories.html")


def single_product(req, pro_id):
    cat = BigmartDb.objects.all()
    first_cat = cat.first()
    data = ProductDb.objects.get(id=pro_id)
    return render(req, "Single_Product.html", {'data': data, 'cat': cat, 'first_cat': first_cat})


def registration_page(req):
    return render(req, "Register.html")


def save_user(request):
    if request.method == 'POST':
        un = request.POST.get('username')
        em = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        obj = RegisterDB(Username=un, Email=em, Password=pass1)
        if RegisterDB.objects.filter(Username=un).exists():
            messages.warning(request, "Username already exists..!")
        else:
            obj.save()
            messages.success(request, "Congrats, your registration succcessful")
        return redirect(registration_page)


def Userlogin(request):
    if request.method == 'POST':
        un = request.POST.get('username')
        pswd = request.POST.get('password')
        if RegisterDB.objects.filter(Username=un, Password=pswd).exists():
            request.session['Username'] = un
            request.session['Password'] = pswd
            messages.success(request, "Login Successful😍")
            return redirect(homepage)
        else:
            messages.error(request, "Check your credentials..!")
            return redirect(registration_page)
    else:
        messages.error(request, "Check credentials..!")
        return redirect(registration_page)


def Userlogout(request):
    del request.session['Username']
    del request.session['Password']
    messages.warning(request, "Logged out")
    return redirect(registration_page)


def AddCart(request):
    if request.method == 'POST':
        un = request.POST.get('username')
        pn = request.POST.get('productname')
        quant = request.POST.get('quantity')
        tp = request.POST.get('totalprice')
        obj = CartDb(Username=un, ProductName=pn, Quantity=quant, TotalPrice=tp)
        obj.save()
        messages.success(request, "Product added to cart")
        return redirect(homepage)


def CartPage(request):
    username = request.session.get('Username')
    if username is not None:
        cat = BigmartDb.objects.all()
        first_cat = cat.first()
        data = CartDb.objects.filter(Username=request.session['Username'])
        subtotal = 0
        shipping_charge = 0
        total = 0
        for d in data:
            subtotal = subtotal + d.TotalPrice
            if subtotal >= 500:
                shipping_charge = 50
            else:
                shipping_charge = 100
            total = subtotal + shipping_charge
        return render(request, "Cart.html",
                      {'data': data, 'total': total, 'subtotal': subtotal, 'shipping_charge': shipping_charge,
                       'cat': cat, 'first_cat': first_cat})
    else:
        messages.error(request, "Please login before accessing the cart..!")
        return render(request, "Register.html")


def delete_item(request, p_id):
    x = CartDb.objects.filter(id=p_id)
    x.delete()
    messages.warning(request, "Product removed to cart")
    return redirect(CartPage)


def userloginpage(request):
    return render(request, "Userlogin.html")


def checkoutpage(request):
    product = CartDb.objects.filter(Username=request.session['Username'])
    if request.method == 'POST':
        un = request.POST.get('username')
        em = request.POST.get('email')
        ph = request.POST.get('phone')
        add = request.POST.get('address')
        desc = request.POST.get('description')
        obj = OrderDB(Username=un, Email=em, Phone=ph, Address=add, Description=desc)
        obj.save()
        return redirect(paymentpage)

    subtotal = 0
    shipping_charge = 0
    total = 0
    for d in product:
        subtotal = subtotal + d.TotalPrice
        if subtotal >= 500:
            shipping_charge = 50
        else:
            shipping_charge = 100
        total = subtotal + shipping_charge
    return render(request, "checkout.html",
                  {'product': product, 'subtotal': subtotal, 'shipping_charge': shipping_charge, 'total': total})


def paymentpage(request):
    # retrieving the orderDB object with the specified ID
    customer = OrderDB.objects.order_by('-id').first()

    # get the payment amount of the specified customer
    payy = customer.TotalPrice

    # get the payment amount to paisa(smallest currency unit)
    amount = int(payy * 100)

    # convert amount to string for  printing
    payy_str = str(amount)

    # printing each character  of the  payemnt  amount
    for i in payy_str:
        print(i)

    if request.method == 'POST':
        order_currency = INR
        client = razorpay.Client(auth=('rzp_test_Xe8qXi9C0xosm3', 'XcZsUeKUQZUqD7FF8xKcZT2H'))
        payment = client.order.create({'amount': amount, 'currency': order_currency, 'payment_capture': '1'})

    return render(request, "payment.html", {'customer': customer, 'payy_str': payy_str})


def subscribe(request):
    if request.method == 'POST':
        em = request.POST.get('email')
        obj = subscribeDB(Email=em)
        obj.save()
        return redirect(ourproducts)


def saveorder(request):
    if request.method == 'POST':
        nm = request.POST.get('name')
        em = request.POST.get('email')
        pl = request.POST.get('place')
        add = request.POST.get('address')
        ph = request.POST.get('phone')
        msg = request.POST.get('message')
        tp = request.POST.get('totalprice')
        obj = OrderDB(Name=nm, Email=em, Place=pl, Address=add, Phone=ph, Message=msg, TotalPrice=tp)
        obj.save()
        return redirect(paymentpage)

# API section