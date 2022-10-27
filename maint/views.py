from django.http import HttpResponse
from django.template import loader

from .models import Vehicle


def index(request):
    vehicle_list = Vehicle.objects.order_by('-assembly_date')
    template = loader.get_template('maint/index.html')
    context = {
        'vehicle_list': vehicle_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, vehicle_id):
    return HttpResponse("You're looking at vehicle %s." % vehicle_id)

