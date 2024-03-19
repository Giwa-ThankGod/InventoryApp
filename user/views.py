from django.shortcuts import render, redirect
from django.contrib.auth import password_validation, authenticate, login
from django.db.models import Q

from django.contrib.auth.models import User
from user.models import Customer, Product

# Create your views here.
def signup(request):
    if request.method == 'GET':

        return render(request, 'signup.html', {'categories': Customer.business_category_choices})
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        business_name = request.POST['business_name']
        business_category = request.POST['business_category']

        # Creating a user
        user = User.objects.create(username=username, email=email) # Create a user with the username
        user.set_password(password) # Assign a password to the user account.
        user.save() # save to database.

        # Creating a customer
        customer = Customer.objects.create(
            user = user,
            business_name = business_name, 
            business_category = business_category, 
        )

        return redirect('signup')
    
def signin(request):
    if request.method == 'GET':
        return render(request, 'signin.html')
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Check if the user with the username and password are valid inputs.
        authenticated_user = authenticate(username=username, password=password)
        if authenticated_user is not None:
            login(request, authenticated_user)
            # Redirect to a success page.
            return redirect('dashboard')
        else:
            # Return an 'invalid login' error message.
            return redirect('signin')

def dashboard(request):
    return render(request, 'dashboard.html')

def add_inventory(request):
    if request.method == 'GET':
        return render(request, 'add_inventory.html')
    elif request.method == 'POST':
        # Extract product details.
        name = request.POST['name']
        description = request.POST['description']
        price = request.POST['price']
        quantity = request.POST['quantity']

        # Create a product based on user entries.
        product = Product.objects.create(
            name = name,
            description = description,
            price = price,
            quantity= quantity,
            customer = Customer.objects.get(user=request.user)
        )

        # Redirect to users inventory page.
        return redirect('view-inventory')
    
def view_inventory(request):
    products = Product.objects.filter(customer__user=request.user)
    
    context = {'products': products}
    return render(request, 'view_inventory.html', context)

def update_inventory(request, product_id):
    # Retrieves the specific product to be updated.
    product = Product.objects.get(id=product_id)

    if request.method == 'GET':
        return render(request, 'add_inventory.html', {'product': product})
    elif request.method == 'POST':
        # Extract product details.
        name = request.POST['name']
        description = request.POST['description']
        price = request.POST['price']
        quantity = request.POST['quantity']

        # Update the product based on user entries.
        product.name = name
        product.description = description
        product.price = price
        product.quantity = quantity
        product.save() # Remember to save the new changes made to the product.

        # Redirect to users inventory page.
        return redirect('view-inventory')

def delete_inventory(request, product_id):
    # Retrieves the specific product to be updated.
    product = Product.objects.get(id=product_id)

    # Deletes the product.
    product.delete()

    # Redirect to users inventory page.
    return redirect('view-inventory')


def search_inventory(request):
    user = User.objects.get(username=request.user)

    search = request.GET.get('search')

    products = Product.objects.filter(
        Q(customer = user.customer) &
        Q(name__icontains = search) |
        Q(description__icontains = search) |
        Q(price__icontains = search)
    )

    context = {'products': products, 'count': products.count()}
    return render(request, 'view_inventory.html', context)




