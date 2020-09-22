from django.shortcuts import render, redirect
from .models import *
from .Forms import OrderForm, CustomerForm, CreateUserForm
from django.forms import inlineformset_factory
from .Filters import OrderFilter
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users, admin_only
from django.contrib.auth.models import Group


@unauthenticated_user
def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            messages.success(request, "Hell yeah Welcome" + username)
            return redirect("login")
    context = {"form": form}
    return render(request, 'Account/register.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def userpage(request):
    orders = request.user.customer.order_set.all()
    total_orders = orders.count()
    delivered = orders.filter(status="Delivered").count()
    pending = orders.filter(status="Pending").count()
    context = {'orders': orders, 'total_orders': total_orders,
               'delivered': delivered, 'pending': pending}
    return render(request, 'Account/user.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def accountSettings(request):
    customer = request.user.customer
    form = CustomerForm(instance=customer)
    if request.method == "POST":
        form = CustomerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, "Account/account_settings.html", context)


@unauthenticated_user
def Login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('homepage')
        else:
            messages.info(request, 'Username or password is incorrect')

    context = {}
    return render(request, 'Account/login.html', context)


def logoutuser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
@admin_only
def homepage(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    total_customer = customers.count()
    total_orders = orders.count()

    delivered = orders.filter(status="Delivered").count()
    pending = orders.filter(status="Pending").count()

    context = {'orders': orders, 'customers': customers, 'total_orders': total_orders,
               'delivered': delivered, 'pending': pending}
    return render(request, 'Account/dashboard.html', context)


@login_required(login_url='login')
@admin_only
def products(request):
    products = Product.objects.all()
    return render(request, 'Account/products.html', {'product': products})


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def customer(request, pk):
    customers = Customer.objects.get(id=pk)
    orders = customers.order_set.all()
    order_count = orders.count()
    myFilter = OrderFilter(request.GET, queryset=orders)
    orders = myFilter.qs
    context = {'customer': customers,
               'orders': orders,
               'order_count': order_count,
               'myFilter': myFilter}
    return render(request, 'Account/customer.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def createOrder(request, pk):
    OrderformSet = inlineformset_factory(Customer, Order, fields=('product', 'status'), extra=10)
    customer = Customer.objects.get(id=pk)
    # form = OrderForm(initial={'customer': customer})
    formset = OrderformSet(queryset=Order.objects.none(), instance=customer)
    if request.method == "POST":
        # form = OrderForm(request.POST)
        formset = OrderformSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('/')

    context = {'formset': formset}  # , 'customer': customer
    return render(request, 'Account/order_form.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'formset': form}
    return render(request, 'Account/order_form.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == "POST":
        order.delete()
        return redirect('/')
    context = {'item': order}
    return render(request, "Account/delete.html", context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def updateCustomer(request, pk):
    customer = Customer.objects.get(id=pk)
    form = CustomerForm(instance=customer)
    if request.method == "POST":
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form, 'customer': customer}
    return render(request, 'Account/update_customer.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def createCustomer(request):
    customer = Customer.objects.all()
    form = CustomerForm()
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form, 'customer': customer}
    return render(request, 'Account/update_customer.html', context)
