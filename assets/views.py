from django.shortcuts import get_object_or_404, render

from .models import Vehicle


def vehicle_list(request):
    vehicle_list = Vehicle.objects.order_by('-assembly_date')
    total = Vehicle.objects.count()
    context = {
        'vehicle_list': vehicle_list,
        'total': total
    }
    return render(request, 'assets/vehicle_list.html', context)

def vehicle_detail(request, vehicle_id):
    vehicle = get_object_or_404(Vehicle, pk=vehicle_id)
    return render(request, 'assets/vehicle_detail.html', {'vehicle': vehicle})

def consumbles(request):
    vehicle_list = Vehicle.objects.order_by('-assembly_date')
    total = Vehicle.objects.count()
    context = {
        'vehicle_list': vehicle_list,
        'total': total
    }
    return render(request, 'assets/vehicle_list.html', context)
