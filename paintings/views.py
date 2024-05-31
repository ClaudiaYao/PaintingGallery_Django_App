from django.shortcuts import render, redirect
# from django.http import HttpResponse
from .models import Painting
from .forms import PaintingForm, ReviewForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .utils import searchPainting, paginatePaintings

# Create your views here.

def paintings(request):
    paintings, search_query = searchPainting(request)
    paintings, custom_range = paginatePaintings(request, paintings, 6)

    context = {"paintings": paintings, "search_query": search_query, "custom_range": custom_range}
    return render(request, "paintings/paintings.html", context)

def painting(request, pk):
    paintObj = Painting.objects.get(id=pk)
    tags = paintObj.tags.all()
    review_form = ReviewForm()

    if request.method == "POST":
        form = ReviewForm(request.POST)
        review = form.save(commit=False)
        review.painting = paintObj
        review.owner = request.user.profile
        review.save()
        paintObj.getVoteScore()
        messages.success(request, "Your review was saved successfully.")
        return redirect("painting", pk = paintObj.id)
        
    return render(request, "paintings/single_painting.html", {'paint': paintObj, "tags": tags, "review_form": review_form})

@login_required(login_url="login-user")
def createPainting(request):
    form = PaintingForm()

    if request.method == "POST":
        form = PaintingForm(request.POST, request.FILES)
        if form.is_valid:
            painting  = form.save(commit=False)
            painting.owner = request.user.profile
            painting.save()
            return redirect("paintings")

    context = {"form": form}
    return render(request, "paintings/painting_form.html", context)

@login_required(login_url="login-user")
def updatePainting(request, pk):
    profile = request.user.profile
    paintObj = profile.painting_set.get(id=pk)
    form = PaintingForm(instance=paintObj)

    if request.method == "POST":
        form = PaintingForm(request.POST, request.FILE, instance=paintObj)
        if form.is_valid:
            form.save()
            return redirect("paintings")

    context = {"form": form}
    return render(request, "paintings/painting_form.html", context)

@login_required(login_url="login-user")
def deletePainting(request, pk):
    profile = request.user.profile
    paintObj = profile.painting_set.get(id=pk)
    context = {"painting": paintObj}

    if request.method == "POST":
        paintObj.delete()
        return redirect("projects")
    return render(request, "paintings/delete_painting.html", context)