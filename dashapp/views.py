from django.shortcuts import render

# Create your views here.


def dashboard(request):
    template = 'dashboard.html'
    
    context = {}
    return render(request, template, context)
