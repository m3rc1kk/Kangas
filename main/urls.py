from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('main/', views.ListProductView.as_view(), name='product-list'),
    path('<int:id>/<slug:slug>/', views.DetailProductView.as_view(), name='product-detail'),
]
