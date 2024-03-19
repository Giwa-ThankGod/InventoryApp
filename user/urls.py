from django.urls import path
from user import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),

    path('dashboard/', views.dashboard, name='dashboard'),

    # Products
    path('add/inventory/', views.add_inventory, name='add-inventory'),
    path('update/inventory/<product_id>/', views.update_inventory, name='update-inventory'),
    path('delete/inventory/<product_id>/', views.delete_inventory, name='delete-inventory'),
    path('search/inventory/', views.search_inventory, name='search-inventory'),
    path('view/inventory/', views.view_inventory, name='view-inventory'),
]