from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render

from .models import Vehicle, LicencePlate


def index(request):
    vehicle_list = Vehicle.objects.order_by('-assembly_date')
    context = {
        'vehicle_list': vehicle_list,
    }
    return render(request, 'maint/index.html', context)

def detail(request, vehicle_id):
    try:
        vehicle = Vehicle.objects.get(pk=vehicle_id)
    except Vehicle.DoesNotExist:
        raise Http404("Vehicle does not exist")
    return render(request, 'maint/detail.html', {'vehicle': vehicle})

