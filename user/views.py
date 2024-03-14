from django.shortcuts import render, redirect
from django.contrib.auth import password_validation

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