# input : aaabbcde
# output : c

# def firstNonRepeatingChar(stringA):
    
#     mapChar = {}
    
#     for char in stringA:
        
#         mapChar[char] = mapChar.get(char, 0) + 1
        
#     for key , value in mapChar.items():
#         if value == 1:
#             return key
# #     return -1

# # input = "aaabbcde"
# print(firstNonRepeatingChar(input))




# app/views.py
from django.shortcuts import render, get_object_or_404
from .models import Product
from django.http import HttpResponse
 
def product_detail(request, product_id):
    # Bug 1: Expecting a single object, but using filter() and checking 
    # if it exists, which is less efficient than get_object_or_404.
    product = Product.objects.filter(id=product_id).exists()
    if product:
        # Bug 2: Assuming the filtered queryset is the product object
        return render(request, 'product_detail.html', {'product': product})
    else:
        return HttpResponse("Product not found", status=404)
 
# def create_product(request):
#     if request.method == 'POST': # Bug 3: Using 'GET' method for creation logic
#         name = request.POST.get('name')
#         price = request.POST.get('price')
#         if name and price:
#             Product.objects.create(name=name, price=price)
#             return HttpResponse({'status': 'Product created'}, status=201) # Bug 4: HttpResponse is not JSON
 
# # project/urls.py
# from django.contrib import admin
# from django.urls import path
# from myapp import views # Assuming the app is named 'myapp'
 
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     # Bug 5: Incorrect URL pattern definition for detail view
#     path('products/<int:id>/', views.product_detail), 
#     path('products/create/', views.create_product),
# ]


# empl = Employee.objects.select_related('department_name').all()

# for emp in empl:
#     print( emp.id, emp.name,emp.department_name, emp.sal)