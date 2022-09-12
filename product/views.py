from django.shortcuts import get_object_or_404, render
from django.views import View
# Create your views here.
from .models import Product,Category
from orders.forms import CartAddForm


class ProductView(View):

    
    def get(self,request,category_slug=None):
        products=Product.objects.filter(available=True)
        categories=Category.objects.filter(is_sub=False)
        if category_slug:
            category=Category.objects.get(slug=category_slug)
            products=products.filter(category=category)
        return render(request,'product/products.html',{'products':products,'categories':categories})




class ProductDetailsView(View):
    form_class=CartAddForm
    def get(self,request,*args,**kwargs):
           
           product=get_object_or_404(Product,id=kwargs['product_id'],slug=kwargs['product_slug']) 
           return render(request,'product/details.html',{'product':product,'form':self.form_class})
























        