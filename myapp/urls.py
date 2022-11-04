from django.urls import path
from .views import show_all_products_page

urlpatterns = [
    path('', show_all_products_page),
]
