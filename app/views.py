from django.shortcuts import render

# Create your views here.
def zomato(request):
    return render(request,'zomato.html')