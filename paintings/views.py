from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def paintings(request):
    return render(request, "paintings/paintings.html")

def painting(request, pk):
    paintObj = None
    for paint in paintings:
        if paint['id'] == pk:
            paintObj = paint 
    return render(request, "paintings/single_painting.html", {'paintObj': paintObj})