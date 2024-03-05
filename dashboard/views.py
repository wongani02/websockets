from django.shortcuts import render, get_object_or_404

from .models import *

# Create your views here.


def index(request):

    qs = Statistic.objects.all()

    context = {
        'qs': qs
    }
    return render(request, 'dashboard/index.html', context)


def dashboard(request, slug):

    statistic = get_object_or_404(Statistic, slug=slug)



    context = {
        'statistic': statistic
    }
    return render(request, 'dashboard/dashboard.html', context)