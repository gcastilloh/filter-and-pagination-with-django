from django.shortcuts import render
from django.core.paginator import Paginator


from .models import Product
from .filters import ProductFilter

# Create your views here.

def show_all_products_page(request):
    context = {}
    filtered_products = ProductFilter(
        request.GET,
        queryset=Product.objects.all(),
    )

    context['filtered_products'] = filtered_products
    # return render(request, 'myapp/show_all_products_page.html', context=context)

    paginated_filtered_products = Paginator(filtered_products.qs, 5)
    page_number = request.GET.get('page')
    product_page_obj = paginated_filtered_products.get_page(page_number)

    context['product_page_obj'] = product_page_obj
    return render(request, 'myapp/show_all_products_page.html', context=context)
