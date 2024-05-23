from django.shortcuts import render, redirect
# from django.http import HttpResponse
from .models import Painting
from .forms import PaintingForm
# Create your views here.


def paintings(request):
    paintings = Painting.objects.all()
    context = {"paintings": paintings}
    return render(request, "paintings/paintings.html", context)

def painting(request, pk):
    paintObj = Painting.objects.get(id=pk)
    tags = paintObj.tags.all()
    return render(request, "paintings/single_painting.html", {'paint': paintObj, "tags": tags})

def createPainting(request):
    form = PaintingForm()

    if request.method == "POST":
        form = PaintingForm(request.POST, request.FILES)
        if form.is_valid:
            form.save()
            return redirect("paintings")

    context = {"form": form}
    return render(request, "paintings/painting_form.html", context)

def updatePainting(request, pk):
    paintObj = Painting.objects.get(id=pk)
    form = PaintingForm(instance=paintObj)

    if request.method == "POST":
        form = PaintingForm(request.POST, request.FILES, instance=paintObj)
        if form.is_valid:
            form.save()
            return redirect("paintings")

    context = {"form": form}
    return render(request, "paintings/painting_form.html", context)

def deletePainting(request, pk):
    projectObj = Painting.objects.get(id=pk)
    context = {"object": projectObj}

    if request.method == "POST":
        projectObj.delete()
        return redirect("projects")
    return render(request, "paintings/delete_painting.html", context)