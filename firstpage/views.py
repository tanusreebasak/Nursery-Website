from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .forms import *
from .models import *
from .filters import OrderFilter
from django.contrib import messages
from .decorators import unauthenticated_user,allowed_users,admin_only
from django.views import View


def post(self,request):
    product = request.POST.get('product')
    cart = request.session.get('cart')
    if cart:
        quantity = cart.get(product)
        if quantity:
            cart[product] = quantity + 1 
        else:
            cart[product] = 1
    else:
        cart={}
        cart['products'] = 1
    request.session['cart'] = cart
    return redirect('user-page')
def get(self,request):
    products = None
    

@unauthenticated_user
def registerPage(request):          
    form = CreateUserForm()
    if request.method=='POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='customer')
            user.groups.add(group)
            Customer.objects.create(user=user,name=user.username)
            messages.success(request, ' Account was created for ' + username)
            return redirect('login')
    context={'form':form}
    return render(request, 'firstpage/register.html' , context)

@unauthenticated_user
def loginPage(request):    
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username= username , password = password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.info(request, 'USername or password is incorrect !!')            
    context={}
    return render(request, 'firstpage/login.html' , context)

def logoutUser(request): 
    logout(request)
    return redirect('login')


@login_required(login_url='login')
@admin_only
def home(request):
    orders= Order.objects.all()
    customers = Customer.objects.all()
    total_customers = customers.count()
    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()  
    context = {'orders':orders,'customers':customers,'total_orders':total_orders,'delivered':delivered,'pending':pending}
    return render(request, 'firstpage/dashboard.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def userPage(request):
    product = request.POST.get('product')
    cart = request.session.get('cart')
    if cart:
        quantity = cart.get(product)
        if quantity:
            cart[product] = quantity + 1 
        else:
            cart[product] = 1
    else:
        cart={}
        cart['products'] = 1
    request.session['cart'] = cart
    orders = request.user.customer.order_set.all()
    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count() 
    context={'orders':orders,'total_orders':total_orders,'delivered':delivered,'pending':pending}
    return render(request, 'firstpage/user.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def accountSettings(request):
    user = request.user.customer
    form = CustomerForm(instance = user)
    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES,instance = user)
        if form.is_valid():
            form.save()
    context={'form':form}
    return render(request, 'firstpage/account_settings.html',context)


def plants(request):
    plants = Plants.objects.all()
    return render(request, 'firstpage/plants.html',{'plants':plants})

def contact(request):
    return render(request, 'firstpage/contact.html')

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def customer(request,pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()
    order_count = orders.count()
    myFilter = OrderFilter(request.GET,queryset=orders)
    orders = myFilter.qs
    context={'customer':customer,'orders':orders,'order_count':order_count,'myFilter': myFilter} 
    return render(request, 'firstpage/customer.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def createOrder(request,pk):
    OrderFormSet = inlineformset_factory(Customer,Order,fields=('plants','status'),extra=5)
    customer = Customer.objects.get(id=pk)
    formset = OrderFormSet(queryset=Order.objects.none(),instance=customer)
    #form = OrderForm(initial={'customer': customer})
    if request.method=='POST':
        #form = OrderForm(request.POST)
        formset = OrderFormSet(request.POST,instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('/')
    context={'formset':formset}
    return render(request, 'firstpage/order_form.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updateOrder(request,pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method=='POST':
        form = OrderForm(request.POST , instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request, 'firstpage/order_form.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deleteOrder(request,pk):
    order = Order.objects.get(id=pk)
    if request.method=='POST':
        order.delete()
        return redirect('/')
    context={'item':order}
    return render(request, 'firstpage/delete.html',context)