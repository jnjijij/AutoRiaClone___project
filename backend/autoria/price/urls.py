from django.urls import path
from . import views

urlpatterns = [
    path('price/', views.AdPriceView.as_view(), name='ad_price'),
]