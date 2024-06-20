from .models import Profile, Skill
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def paginateProfiles(request, profiles, num_per_page):
    page = request.GET.get("page")
    paginator = Paginator(profiles, num_per_page)

    try:
        user_profiles = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        user_profiles = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        user_profiles = paginator.page(page)

    left_index = max(int(page)-3, 1)
    right_index = min(left_index + 4, paginator.num_pages + 1)
    custom_range = range(left_index, right_index)
    return user_profiles, custom_range


def searchProfile(request):
    
    search_query = ""

    if request.GET.get("search_query"):
        search_query = request.GET.get("search_query")

    skills = Skill.objects.filter(name__iexact=search_query)
    profiles = Profile.objects.distinct().filter(
        Q(username__icontains=search_query) | 
        Q(short_intro__icontains=search_query) |
        Q(skill__in=skills))
    
    return profiles, search_query