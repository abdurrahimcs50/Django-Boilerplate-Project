from django.shortcuts import render

# Create your views here.

def MainHome(request):
    return render(request, 'main/Home.html')