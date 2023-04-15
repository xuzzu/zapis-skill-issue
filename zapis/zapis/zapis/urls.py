"""
URL configuration for zapis project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from zapis_api.views import SaleView, SupplyView, CreateSaleView, CreateSupplyView, UpdateSupplyView, UpdateSaleView, \
    DeleteSaleView, DeleteSupplyView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('sales/', SaleView.as_view()),
    path('sales/<int:id>/', SaleView.as_view()),
    path('sales/create/', CreateSaleView.as_view()),
    path('sales/<int:id>/update/', UpdateSaleView.as_view()),
    path('sales/<int:id>/delete/', DeleteSaleView.as_view()),

    path('supplies/', SupplyView.as_view()),
    path('supplies/<int:id>/', SupplyView.as_view()),
    path('supplies/create/', CreateSupplyView.as_view()),
    path('supplies/<int:id>/update/', UpdateSupplyView.as_view()),
    path('supplies/<int:id>/delete/', DeleteSupplyView.as_view()),
]
