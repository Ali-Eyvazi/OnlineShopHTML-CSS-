from django.urls import path
from . import views


app_name='product'

urlpatterns=[

    path('',views.ProductView.as_view(),name='products'),
    path('details/<int:product_id>/<slug:product_slug>',views.ProductDetailsView.as_view(),name='details'),
    path('category/<slug:category_slug>',views.ProductView.as_view(),name='category_view'),
    
]





















