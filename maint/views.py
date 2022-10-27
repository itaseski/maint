from django.http import HttpResponse

from .models import Vehicle


def index(request):
    vehicle_list = Vehicle.objects.order_by('-assembly_date')
    output = ', '.join([vehicle.vin for vehicle in vehicle_list])
    return HttpResponse(output)

def detail(request, vehicle_id):
    return HttpResponse("You're looking at vehicle %s." % vehicle_id)

