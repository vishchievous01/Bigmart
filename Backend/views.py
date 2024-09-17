from django.shortcuts import render, redirect
from Backend.models import BigmartDb, ProductDb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from WebApp.models import ContactDb
from django.contrib import messages


# Create your views here.

def index_page(req):
    return render(req, "index.html")


def category_page(req):
    return render(req, "Category.html")


def save_category(request):
    if request.method == "POST":
        nm = request.POST.get('name')
        desc = request.POST.get('descrip')
        img = request.FILES['image']
        obj = BigmartDb(C_name=nm, Descptn=desc, C_image=img)
        obj.save()
        messages.success(request, "Category saved successfully..!")
        return redirect(category_page)


def display_category(req):
    data = BigmartDb.objects.all()
    return render(req, "Display_category.html", {'data': data})


def edit_category(req, catid):
    cat = BigmartDb.objects.get(id=catid)
    return render(req, "Edit_Category.html", {'cat': cat})


def update_category(request, catid):
    if request.method == "POST":
        nm = request.POST.get('name')
        desc = request.POST.get('descrip')
    try:
        img = request.FILES['image']
        fs = FileSystemStorage()
        file = fs.save(img.name, img)
    except MultiValueDictKeyError:
        file = BigmartDb.objects.get(id=catid).C_image
    BigmartDb.objects.filter(id=catid).update(C_name=nm, Descptn=desc, C_image=file)
    messages.success(request, "Updated")
    return redirect(display_category)


def delete_category(request ,catid):
    data = BigmartDb.objects.filter(id=catid)
    data.delete()
    messages.error(request, "Deleted..!")
    return redirect(display_category)


def login_page(request):
    return render(request, "admin_login.html")


def admin_page(request):
    if request.method == "POST":
        un = request.POST.get('username')
        pwd = request.POST.get('password')
        if User.objects.filter(username__contains=un).exists():
            x = authenticate(username=un, password=pwd)
            if x is not None:
                login(request, x)
                request.session['username'] = un
                request.session['password'] = pwd
                messages.success(request, "Welcome..!")
                return redirect(index_page)
            else:
                messages.error(request, "Invalid password...!")
                return redirect(login_page)
        else:
            messages.warning(request, "User not found..!")
            return redirect(login_page)


def AdminLogout(request):
    del request.session['username']
    del request.session['password']
    return redirect(login_page)


def product_page(req):
    cat = BigmartDb.objects.all()
    return render(req, "Products.html", {'cat': cat})


def save_product(request):
    if request.method == "POST":
        cat = request.POST.get('category')
        nm = request.POST.get('pname')
        pr = request.POST.get('price')
        des = request.POST.get('descrip')
        img = request.FILES['image']
        obj = ProductDb(Category=cat, P_name=nm, Price=pr, Description=des, P_image=img)
        obj.save()
        return redirect(product_page)


def display_product(req):
    data = ProductDb.objects.all()
    return render(req, "Display_product.html", {'data': data})


def edit_product(req, proid):
    pro = ProductDb.objects.get(id=proid)
    cat = BigmartDb.objects.all()
    return render(req, "Edit_product.html", {'pro': pro, 'cat': cat})


def delete_product(x, proid):
    x = ProductDb.objects.filter(id=proid)
    x.delete()
    return redirect(display_product)


def update_product(request, proid):
    if request.method == "POST":
        cat = request.POST.get('category')
        nm = request.POST.get('pname')
        pr = request.POST.get('price')
        des = request.POST.get('descrip')
    try:
        img = request.FILES['image']
        fs = FileSystemStorage()
        file = fs.save(img.name, img)
    except MultiValueDictKeyError:
        file = ProductDb.objects.get(id=proid).P_image
    ProductDb.objects.filter(id=proid).update(Category=cat, P_name=nm, Price=pr, Description=des, P_image=file)
    return redirect(display_product)


def contact_details(req):
    data = ContactDb.objects.all()
    return render(req, "ContactData.html", {'data': data})


def delete_contact(x, delid):
    x = ContactDb.objects.filter(id=delid)
    x.delete()
    return redirect(contact_details)






