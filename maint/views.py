from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the maint index.")

def detail(request, vehicle_id):
    return HttpResponse("You're looking at vehicle %s." % vehicle_id)

