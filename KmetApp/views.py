from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from KmetApp.models import User, Selling, Basket
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


#TO DOOO!!!!
def add_orderS(request):
    """Add order for Selling"""
    print("Sup")
    if request.method == 'POST':
        print(request.POST)
    return redirect("Hello")


def my_sellings(request):
    """View for Users Sellings"""
    user = User.objects.get(id=request.user.id)
    sellings = Selling.objects.filter(seller=user).exclude(is_Active=False)
    return render(request, 'Sellings/MySellings.html', {'sellings': sellings})


def disable_selling(request):
    """Function to disable an active selling"""
    selling = request.GET.get('id')
    disable = Selling.objects.get(id=selling)
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