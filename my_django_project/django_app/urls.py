from .views import CarListView, CarDetailView
from django.urls import path

urlpatterns = [
    path('', CarListView.as_view(), name='car_list'),
    path('<int:pk>/', CarDetailView.as_view(), name='car_detail')
]