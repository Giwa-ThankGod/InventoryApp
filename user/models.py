from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # Customized Fields.
    business_category_choices = (
        ('Supermarket', 'Supermarket'),
        ('Pharmacy', 'Pharmacy'),
        ('Electronics', 'Electronics')
    )
    phone = models.CharField(max_length=20)
    business_name = models.CharField(max_length=100)
    business_category = models.CharField(max_length=50, choices=business_category_choices)

    def __str__(self):
        return self.business_name

class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    price = models.FloatField(default=0.0)
    quantity = models.IntegerField(default=0)

    # Connecting product to a customer.
    customer = models.ForeignKey(Customer, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name