from django.urls import path
from api import views

urlpatterns = [
    path('', views.test_api, name='test_api'),
    path('inventory/', views.inventory, name='inventory'),
    path('inventory/<product_id>/', views.get_update_inventory, name='get-update-inventory'),
]