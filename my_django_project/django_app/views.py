from .models import CarProduct
from django.views.generic import ListView, DetailView


class CarListView(ListView):
    queryset = CarProduct.objects.all()
    context_object_name = 'cars'
    template_name = 'car_test.html'


class CarDetailView(DetailView):
    queryset = CarProduct.objects.all()
    context_object_name = 'car'
    template_name = 'car_detail.html'