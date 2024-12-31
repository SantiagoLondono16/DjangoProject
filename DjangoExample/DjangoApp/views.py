from django.shortcuts import render
from django.http import HttpResponse
from .forms import InputForm

# Create your views here.
def FormView(request):
    form = InputForm()
    context = {'form': form}
    return render(request, 'FormView.html', context)