from django.http import HttpResponse
from django.shortcuts import render
import datetime


def weapon(request):
        now = datetime.datetime.now()
        context = {'like':'武器小百科',  'now':now}
        return render(request, 'weapon/weapon.html', context)
# Create your views here.
