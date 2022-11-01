from django.shortcuts import render

from django.shortcuts import get_object_or_404, render

from .models import Screws, DIN933, DIN931, DIN6921, DIN912, DIN7981, ISO14583, DIN7500D

def screws(request):
    screws_list = Screws.objects.all()
    context = {
        'screws_list': screws_list,
    }
    return render(request, 'fasteners/screws/screws.html', context)


def din933(request):
    din933_list = DIN933.objects.order_by('thread_length')
    context = {
        'din933_list': din933_list,
    }
    return render(request, 'fasteners/screws/din933.html', context)

def din933_detail(request, din933_id):
    din933 = get_object_or_404(DIN933, pk=din933_id)
    return render(request, 'fasteners/screws/din933_detail.html', {'din933': din933})

def din931(request):
    din931_list = DIN931.objects.order_by('thread_length')
    context = {
        'din931_list': din931_list,
    }
    return render(request, 'fasteners/screws/din931.html', context)

def din931_detail(request, din931_id):
    din931 = get_object_or_404(DIN931, pk=din931_id)
    return render(request, 'fasteners/screws/din933_detail.html', {'din931': din931})

def din6921(request):
    din6921_list = DIN6921.objects.order_by('thread_length')
    context = {
        'din6921_list': din6921_list,
    }
    return render(request, 'fasteners/screws/din6921.html', context)

def din6921_detail(request, din6921_id):
    din6921 = get_object_or_404(DIN6921, pk=din6921_id)
    return render(request, 'fasteners/screws/din6921_detail.html', {'din6921': din6921})



def din912(request):
    din912_list = DIN912.objects.order_by('thread_length')
    context = {
        'din912_list': din912_list,
    }
    return render(request, 'fasteners/screws/din912.html', context)

def din912_detail(request, din912_id):
    din912 = get_object_or_404(DIN912, pk=din912_id)
    return render(request, 'fasteners/screws/din912_detail.html', {'din912': din912})

def din7981(request):
    din7981_list = DIN7981.objects.order_by('-screw_length')
    context = {
        'din7981_list': din7981_list,
    }
    return render(request, 'fasteners/screws/din7981.html', context)

def iso14583(request):
    iso14583_list = ISO14583.objects.values()
    context = {
        'iso14583_list': iso14583_list,
    }
    return render(request, 'fasteners/screws/iso14583.html', context)

def din7500D(request):
    din7500D_list = DIN7500D.objects.values()
    context = {
        'din7500D_list': din7500D_list,
    }
    return render(request, 'fasteners/screws/din7500D.html', context)



 
