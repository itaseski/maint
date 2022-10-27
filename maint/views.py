from django.http import HttpResponse
from django.shortcuts import render

from .models import Vehicle


def index(request):
    vehicle_list = Vehicle.objects.order_by('-assembly_date')
    context = {
        'vehicle_list': vehicle_list,
    }
    return render(request, 'maint/index.html', context)

def detail(request, vehicle_id):
    return HttpResponse("You're looking at vehicle %s." % vehicle_id)

