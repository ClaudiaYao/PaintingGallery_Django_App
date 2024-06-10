from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from .models import Profile, Skill
from django.db.models import Q
from django.contrib import messages
from .forms import CustomUserCreationForm, ProfileForm, SkillForm, MessageForm
from django.contrib.auth.decorators import login_required
from .utils import searchProfile, paginateProfiles

# Create your views here.
def loginUser(request):
    page = "login"
    if request.user.is_authenticated:
        return redirect("profiles")

    if request.method == "POST":
        username = request.POST['username'].lower()
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(request.GET['next'] if "next" in request.GET else 'account')
        else:
            messages.error(request, "User name or password does not exist!")
    return render(request, "users/login_register.html", {"page": page})

def registerUser(request):
    page = "register"
    form = CustomUserCreationForm()

    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, "User account was created.")
            login(request, user)
            return redirect("single-profile")
        else:
            messages.error(request, "Error has occured during registration.")

    context = {"page": page, "form": form}
    return render(request, "users/login_register.html", context)

def logoutUser(request):
    logout(request)
    messages.info(request, "User was logged out.")

    return redirect("login-user")
    # return render(request, "users/login_register.html", context = {"page": "login"})

def profiles(request):
    profiles, search_query = searchProfile(request)
    profiles, custom_range = paginateProfiles(request, profiles, 3)

    context = {"profiles": profiles, "search_query": search_query, "custom_range": custom_range}
    return render(request, "users/profiles.html", context)

def userProfile(request, pk):
    user_profile = Profile.objects.get(id=pk)
    top_skills = user_profile.skill_set.all().exclude(description__exact="")
    other_skills = user_profile.skill_set.all().filter(description__exact="")
    context = {"profile": user_profile, "top_skills": top_skills, "other_skills": other_skills}
    return render(request, "users/single_profile.html", context)

@login_required(login_url="login-user")
def userAccount(request):
    profile = request.user.profile
    skills = profile.skill_set.all()
    context = {"profile": profile, "skills": skills}
    return render(request, "users/account.html", context)

@login_required(login_url="login-user")
def editAccount(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)
    if request.method == "POST":
        form = ProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("account")
        else:
            messages.error(request, "Error has occured during editing profile.")

    context = {"profile": profile, "form": form}
    return render(request, "users/profile_form.html", context)

@login_required(login_url="login-user")
def createSkill(request):
    page = "create"
    profile = request.user.profile
    form = SkillForm()    

    if request.method == "POST":
        form = SkillForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.owner = profile
            skill.save()     
            messages.success(request, "new skill was created.")       
            return redirect("account")
    context = {"form": form, "page": page}
    return render(request, "users/skill_form.html", context)

@login_required(login_url="login-user")
def editSkill(request, pk):
    page = "edit"
    profile = request.user.profile
    skill = profile.skill_set.get(id=pk)
    form = SkillForm(instance = skill)

    if request.method == "POST":
        form = SkillForm(request.POST, instance=skill)
        if form.is_valid():
            form.save()
            messages.success(request, "Skill was updated.") 
            return redirect("account")
    context = {"form": form, "skill": skill, "page": page}
    return render(request, "users/skill_form.html", context)


@login_required(login_url="login-user")
def deleteSkill(request, pk):
    profile = request.user.profile
    skill = profile.skill_set.get(id=pk)
    context = {"skill": skill}

    if request.method == "POST":
        skill.delete()
        messages.success(request, "Skill was deleted successfully.")
        return redirect("account")
    return render(request, "users/delete_skill.html", context)

@login_required(login_url="login-user")
def inbox(request):
    profile = request.user.profile
    # profile is foreign key to both sender and recipients field of Message, so use "related_name" to differentiate them
    messageRequest = profile.messages.all()
    unreadCount = messageRequest.filter(is_read=False).count()

    context ={"messageRequest": messageRequest, "unreadCount": unreadCount}
    return render(request, "users/inbox.html", context)


@login_required(login_url="login-user")
def viewMessage(request, pk):
    profile = request.user.profile
    message = profile.messages.all().get(id=pk)
    if message.is_read is False:
        message.is_read = True
        message.save()
    context ={"message": message}
    return render(request, "users/message.html", context)


# @login_required(login_url="login-user")
def createMessage(request, pk):
    recipient_profile = Profile.objects.get(id=pk)
    form = MessageForm()

    try:
        sender = request.user.profile
    except:
        sender = None

    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.sender = sender
            message.recipient = recipient_profile
            
            if sender:
                message.name = sender.username
                message.email = sender.email
            message.save()     
            messages.success(request, "new message was created.")       
            return redirect("single-profile", pk=recipient_profile.id)
        else:
            print("wrong form input")
        
    context = {"form": form, "recipient_profile_id": recipient_profile.id}
    return render(request, "users/message_form.html", context)