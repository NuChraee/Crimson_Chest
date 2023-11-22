import json
from django.shortcuts import render
from django.http import HttpResponseNotFound, HttpResponseRedirect
from main.forms import Item,ProductForm
from django.urls import reverse
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages  
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.shortcuts import redirect
from .models import Item
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse


# Create your views here.
@login_required(login_url='/login')
def show_main(request):
    products = Item.objects.filter(user=request.user)

    context = {
        'appname' : 'Crimson_Chest',
        'name': request.user.username,
        'class': 'PBP C', # Kelas PBP kamu
        'products': products,
        'last_login': request.COOKIES.get('last_login'),
        'product_count': Item.objects.filter(user=request.user).count()
    }

    return render(request, "main.html", context)

def increase_stock(request, product_id):
    product = Item.objects.get(pk=product_id)
    product.amount += 1
    product.save()
    return HttpResponseRedirect(reverse('main:show_main'))

def decrease_stock(request, product_id):
    product = Item.objects.get(pk=product_id)
    product.amount -= 1
    if product.amount <= 0:
        product.delete()
        return redirect('main:show_main') 
    else:
        product.save()
    return HttpResponseRedirect(reverse('main:show_main'))

def delete_product(request, product_id):
    Item.objects.get(pk=product_id).delete()
    return HttpResponseRedirect(reverse('main:show_main'))

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product = form.save(commit=False)
        product.user = request.user
        product.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "create_product.html", context)

def show_xml(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Item.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = Item.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main")) 
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
    context = {}
    return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def edit_product(request, id):
    # Get product berdasarkan ID
    product = Item.objects.get(pk = id)

    # Set product sebagai instance dari form
    form = ProductForm(request.POST or None, instance=product)

    if form.is_valid() and request.method == "POST":
        # Simpan form dan kembali ke halaman awal
        form.save()
        return HttpResponseRedirect(reverse('main:show_main'))

    context = {'form': form}
    return render(request, "edit_product.html", context)

def get_product_json(request):
    product_item = Item.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize('json', product_item))


@csrf_exempt
def add_product_ajax(request):
    if request.method == 'POST':
        name = request.POST.get("name")
        price = request.POST.get("price")
        description = request.POST.get("description")
        sell = request.POST.get("sell")
        amount = request.POST.get("amount")
        modifiers = request.POST.get("modifiers")
        user = request.user

        new_product = Item(name=name, price=price, description=description, user=user, sell=sell, modifiers=modifiers, amount=amount)
        new_product.save()

        return HttpResponse(b"CREATED", status=201)

    return HttpResponseNotFound()

@csrf_exempt
def delete_product_ajax(request, product_id):
    if request.method == 'POST':
        try:
            product = Item.objects.get(pk=product_id)
            product.delete()
            return JsonResponse({'status': 'success', 'message': 'Product successfully deleted'})
        except Item.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Product not found'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

@csrf_exempt
def decrease_product_ajax(request, product_id):
    try:
        product = Item.objects.get(pk=product_id)
        product.amount -= 1
        if product.amount <= 0:
            product.delete()
            return JsonResponse({'status': 'deleted'})
        else:
            product.save()
        return JsonResponse({'status': 'success'})
    except Item.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Product not found'})
    
@csrf_exempt
def add_amount_ajax(request, product_id):
    try:
        product = Item.objects.get(pk=product_id)
        product.amount += 1
        product.save()
        return JsonResponse({'status': 'success'})
    except Item.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Product not found'})

@csrf_exempt
def edit_product_ajax(request, product_id):
    if request.method == 'POST':
        try:
            product = Item.objects.get(pk=product_id)
            for key, value in request.POST.items():
                if hasattr(product, key):
                    setattr(product, key, value)
            product.save()
            return JsonResponse({'status': 'success', 'message': 'Product successfully updated'})
        except Item.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Product not found'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

@csrf_exempt
def create_product_flutter(request):
    if request.method == 'POST':
        
        data = json.loads(request.body)

        new_product = Item.objects.create(
            user = request.user,
            name = data["name"],
            price = int(data["price"]),
            amount = int(data["amount"]),
            description = data["description"],
            modifiers = data["modifiers"],
        )

        new_product.save()

        return JsonResponse({"status": "success"}, status=200)
    else:
        return JsonResponse({"status": "error"}, status=401)