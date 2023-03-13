from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .models import Timer
from .forms import TimeForm
from django.utils import timezone

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
	
def time_edit(request, pk):
	print("Primary key: ", pk)
	times = get_object_or_404(Timer, pk=pk)
	if request.method == "POST":
		form = TimeForm(request.POST, instance=times)
		if form.is_valid():
		    times = form.save(commit=False)
		    times.date = timezone.now()
		    times.save()
		    return redirect('times_list')
	else:
		form = TimeForm(instance=times)
	return render(request, 'timer/time_edit.html', {'form': form, 'times': times})
