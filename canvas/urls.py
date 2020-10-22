from django.urls import path

from . import views

app_name = 'console'

urlpatterns = [
    path('product-list/',
         views.ProductListView.as_view(), name='product-list'),

    path('product-customize/',
         views.ProductCustomizeView.as_view(), name='product-customize'),
]
