from django.shortcuts import render

def attackhelicopter(request):
            context = {'like':'戰鬥直昇機', }
            return render(request, 'attackhelicopter/attackhelicopter.html', context)