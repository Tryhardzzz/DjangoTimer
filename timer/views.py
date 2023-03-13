from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Timer
from .forms import TimeForm

def get(request):
        form = TimeForm()
        times = Timer.objects.order_by('-date')
        return render(request, 'timer/times_list.html', {'form': form, 'times': times})

def times_list(request):
        form = TimeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('times_list')
        times = Timer.objects.order_by('-date')
        return render(request, 'timer/times_list.html', {'form': form, 'times': times})
        
def time_detail(request, pk):
	form = TimeForm(request.POST)
	times = get_object_or_404(Timer, pk=pk)
	return render(request, 'timer/time_detail.html', {'form': form, 'times': times})
