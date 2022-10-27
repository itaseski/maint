from django.shortcuts import get_object_or_404, render

from .models import Vehicle, LicencePlate


def index(request):
    vehicle_list = Vehicle.objects.order_by('-assembly_date')
    context = {
        'vehicle_list': vehicle_list,
    }
    return render(request, 'maint/index.html', context)

def detail(request, vehicle_id):
    vehicle = get_object_or_404(Vehicle, pk=vehicle_id)
    return render(request, 'maint/detail.html', {'vehicle': vehicle})