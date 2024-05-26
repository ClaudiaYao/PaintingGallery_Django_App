from django.shortcuts import render
from .models import Profile

# Create your views here.

def profiles(request):
    context = {"profiles": Profile.objects.all()}
    return render(request, "users/profiles.html", context)

def userProfile(request, pk):
    user_profile = Profile.objects.get(id=pk)
    top_skills = user_profile.skill_set.all().exclude(description__exact="")
    other_skills = user_profile.skill_set.all().filter(description__exact="")
    context = {"profile": user_profile, "top_skills": top_skills, "other_skills": other_skills}
    return render(request, "users/single_profile.html", context)