from django.shortcuts import render
from django.http.response import JsonResponse

from user.models import Product, Customer
from api.serializers import ProductSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view

# Defining Authentication for our view functions
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import authentication_classes, permission_classes

# Create your views here.
def test_api(request):
    data = {
        'number_of_students': 3,
        'students': [
            {
                'name': 'Excel',
                'gender': 'male'
            },
            {
                'name': 'Arinze',
                'gender': 'male'
            },
            {
                'name': 'Elliot',
                'gender': 'male'
            }
        ]
    }
    
    return JsonResponse(data)

# Creating API Endpoints for the Inventory App
@api_view(['GET', 'POST']) # Added so that django can handle this view as a DRF API view.
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def inventory(request):
    if request.method == 'GET':
        try:
            # retrieve all the inventory for a specific user(logged in user).
            products = Product.objects.filter(customer__user=request.user)

            # Serialize the Products in the inventory.
            serializer = ProductSerializer(products, many=True)

            context = {
                'status': 'success',
                'inventory': serializer.data
            }
        except Exception as error:
            context = {
                'status': 'failed',
                'message': 'user must be authenticated to access this endpoint'
            }

        # return JsonResponse(context) # We can also use the default django Json Response
        return Response(context)
    elif request.method == 'POST':
        # Extract product details.
        name = request.data['name']
        description = request.data['description']
        price = request.data['price']
        quantity = request.data['quantity']

        # Create a product based on user entries.
        product = Product.objects.create(
            name = name,
            description = description,
            price = price,
            quantity= quantity,
            customer = Customer.objects.get(user=request.user)
        )

        # Serialize the users new product.
        serializer = ProductSerializer(product)

        context = {
            'status': 'success',
            'created': True,
            'inventory': serializer.data
        }

        return Response(context)
    

@api_view(['GET', 'PATCH', 'DELETE'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def get_update_inventory(request, product_id:int):
    try:
        product = Product.objects.get(id=product_id, customer__user=request.user)
    except Product.DoesNotExist:
        context = {
            'status': 'failed',
            'message': 'Product with id {} does not exist!!!'.format(product_id)
        }
        return Response(context)

    if request.method == 'GET':
        # Serialize the Products in the inventory.
        serializer = ProductSerializer(product)
        context = {
            'status': 'success',
            'product': serializer.data
        }
        return Response(context)
    
    elif request.method == 'PATCH':
        # Extract product details.
        name = request.data.get('name', None)
        description = request.data.get('description', None)
        price = request.data.get('price', None)
        quantity = request.data.get('quantity', None)  

        # Update fields only when the user submits a new data for that field
        product.name = name if name else product.name
        product.description = description if description else product.description
        product.price = price if price else product.price
        product.quantity= quantity if quantity else product.quantity

        product.save()

        # Serialize the users product.
        serializer = ProductSerializer(product)

        context = {
            'status': 'success',
            'created': False,
            'inventory': serializer.data
        }

        return Response(context)
    
    elif request.method == 'DELETE':
        product.delete()

        # Serialize the users product.
        serializer = ProductSerializer(product)

        context = {
            'status': 'success',
            'product': serializer.data
        }

        return Response(context)