from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from KmetApp.models import User, Selling, Basket, Order_Selling, Order_Basket
import datetime
from django.shortcuts import redirect
from KmetApp.forms import UserForm, UserEditForm, SellingForm, BasketForm
from django.views.decorators.csrf import csrf_exempt

# Create your views here.


def home(request):
    """Return Index HTML"""
    return render(request, 'index.html')


def loginview(request):
    """Return LogIn HTML"""
    return render(request, 'User/LogIn.html')


def register_user(request):
    """Registration User Handler"""
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('KmetApp:home')
        else:
            return render(request, 'User/Registration.html', {'form': form})
    else:
        return render(request, 'User/Registration.html')


def logon(request):
    """Log In User Handler"""
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('KmetApp:home')
        else:
            return render(request, 'User/LogIn.html', {'user': username})
    return render(request, 'User/LogIn.html')


def logoff(request):
    """Log out user"""
    logout(request)
    return redirect('KmetApp:home')


def add_selling(request):
    """Add Selling"""
    form = SellingForm()
    if request.method == 'POST':
        form = SellingForm(request.POST, request.FILES)
        if form.is_valid():
            bbb = form.save(commit=False)
            seller = User.objects.get(id=request.user.id)
            bbb.seller = seller
            bbb.save()
            return render(request, 'Sellings/Selling.html')
        else:
            return render(request, 'Sellings/Add_Selling.html', {'form': form})
    else:
        return render(request, 'Sellings/Add_Selling.html')


def edit_user(request):
    """"Edit User"""
    form = UserEditForm()
    if request.method == 'POST':
        form = UserEditForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('KmetApp:home')
        else:
            return render(request, 'User/Edit.html', {'form': form})
    else:
        return render(request, 'User/Edit.html')


@csrf_exempt
def search_selling(request):
    """Search Sellings in database"""
    if request.method == 'POST':
        search_term = request.POST['search_term']
        if request.user.is_authenticated():
            user = User.objects.get(id=request.user.id)
            sellings = Selling.objects.filter(name__icontains=search_term).exclude(quantity=0).exclude(seller=user).exclude(is_Active=False)
            return render(request, 'Sellings/Selling.html', {'sellings': sellings})
        else:
            sellings = Selling.objects.filter(name__icontains=search_term).exclude(quantity=0).exclude(is_Active=False)
            return render(request, 'Sellings/Selling.html', {'sellings': sellings})
    else:
        return render(request, 'Sellings/Selling.html')


def add_orderS(request):
    """Add order for Selling"""
    if request.method == 'POST':
        quantity = int(request.POST['quantity'])
        selling = Selling.objects.get(id=request.POST['selling'])
        user = User.objects.get(id=request.user.id)
        if(selling.quantity-quantity >= 0):
            selling.quantity = selling.quantity - quantity
            selling.save()
            order = Order_Selling.objects.create(price_Order=selling.price*quantity, quantity_Order=quantity,
            selling=selling, buyer=user)
        else:
            return redirect('KmetApp:search_selling')
        return redirect('KmetApp:search_selling')


def my_sellings(request):
    """View for Users Sellings"""
    user = User.objects.get(id=request.user.id)
    sellings = Selling.objects.filter(seller=user).exclude(is_Active=False)
    return render(request, 'Sellings/MySellings.html', {'sellings': sellings})


def disable_selling(request):
    """Function to disable an active selling"""
    selling = request.GET.get('id')
    disable = Selling.objects.get(id=selling)
    if(disable.seller.id == request.user.id):
        disable.is_Active = False
        disable.save()
    return redirect('KmetApp:my_sellings')


def add_basket(request):
    """Add Basket"""
    form = BasketForm()
    if request.method == 'POST':
        form = BasketForm(request.POST, request.FILES)
        if form.is_valid():
            bbb = form.save(commit=False)
            seller = User.objects.get(id=request.user.id)
            bbb.seller = seller
            bbb.save()
            return render(request, 'Basket/Basket.html')
        else:
            return render(request, 'Basket/Add_Basket.html', {'form': form})
    else:
        return render(request, 'Basket/Add_Basket.html')


@csrf_exempt
def search_basket(request):
    """Search Basket in database"""
    if request.method == 'POST':
        search_term = request.POST['search_term']
        if request.user.is_authenticated():
            user = User.objects.get(id=request.user.id)
            baskets = Basket.objects.filter(name__icontains=search_term).exclude(quantity=0).exclude(seller=user).exclude(is_Active=False).exclude(total_Amount=0)
            return render(request, 'Basket/Basket.html', {'baskets': baskets})
        else:
            baskets = Basket.objects.filter(name__icontains=search_term).exclude(quantity=0).exclude(is_Active=False).exclude(total_Amount=0)
            return render(request, 'Basket/Basket.html', {'baskets': baskets})
    else:
        return render(request, 'Basket/Basket.html')


def my_OrderSellings(request):
    """Returns the view with all submited Orders"""
    user = User.objects.get(id=request.user.id)
    orders = Order_Selling.objects.filter(buyer=user)
    return render(request, 'OrderSellings/MyOrders.html', {'orders': orders})


def undoneOrder(request):
    """"Display All undone Orders for a Selling"""
    user = User.objects.get(id=request.user.id)
    orders = Order_Selling.objects.filter(selling__seller=user, is_Completed=False)
    return render(request, 'OrderSellings/UnCompletedOrders.html', {'orders': orders})


def doneOrder(request):
    """"Display All done Orders for a Selling"""
    user = User.objects.get(id=request.user.id)
    orders = Order_Selling.objects.filter(selling__seller=user, is_Completed=True)
    return render(request, 'OrderSellings/CompletedOrders.html', {'orders': orders})


def editSelling(request):
    """"Action where you can edit an active selling"""
    if request.method == 'POST':
        selling = Selling.objects.get(id=request.POST['selling'])
        if(selling.seller.id == request.user.id):
            selling.name = request.POST['name']
            selling.price = request.POST.get('price', False)
            selling.description = request.POST['description']
            selling.origin = request.POST['origin']
            selling.quantity = request.POST['quantity']
            if(request.POST['picture']):
                selling.picture = request.POST['picture']
            selling.save()
    return redirect('KmetApp:my_sellings')


def complete_orderSelling(request):
    """Function to complete an active order"""
    id = request.GET.get('id')
    user = User.objects.get(id=request.user.id)
    order = Order_Selling.objects.get(id=id, selling__seller=user)
    if(order):
        order.is_Completed = True
        order.date_Completed = datetime.now()
        order.save()
    return redirect('KmetApp:undoneOrder')


def add_orderB(request):
    """Add order for Selling"""
    if request.method == 'POST':
        quantity = int(request.POST['quantity'])
        frequency = int(request.POST['frequency'])
        basket = Basket.objects.get(id=request.POST['basket'])
        user = User.objects.get(id=request.user.id)
        if(basket.quantity-quantity >= 0):
            basket.quantity = basket.quantity - quantity
            basket.frequency = frequency
            basket.save()
            order = Order_Basket.objects.create(price_Order=basket.price*quantity, quantity_Order=quantity, frequency=frequency,
            basket=basket, buyer=user)
        else:
            return redirect('KmetApp:search_basket')
        return redirect('KmetApp:search_basket')


def disable_basket(request):
    """Function to disable an active basket"""
    basket = request.GET.get('id')
    disable = Basket.objects.get(id=basket)
    if(disable.seller.id == request.user.id):
        disable.is_Active = False
        disable.save()
    return redirect('KmetApp:my_sellings')


def my_baskets(request):
    """View for Users Baskets"""
    user = User.objects.get(id=request.user.id)
    baskets = Basket.objects.filter(seller=user).exclude(is_Active=False)
    return render(request, 'Basket/MyBasket.html', {'baskets': baskets})


def editBasket(request):
    """"Action where you can edit an active selling"""
    if request.method == 'POST':
        basket = Basket.objects.get(id=request.POST['basket'])
        if(basket.seller.id == request.user.id):
            basket.name = request.POST['name']
            basket.price = request.POST.get('price', False)
            basket.total_Amount = request.POST.get('total_Amount', False)
            basket.description = request.POST['description']
            basket.origin = request.POST['origin']
            basket.quantity = request.POST['quantity']
            if(request.POST['picture']):
                basket.picture = request.POST['picture']
            basket.save()
    return redirect('KmetApp:my_baskets')