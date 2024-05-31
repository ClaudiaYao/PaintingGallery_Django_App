from .models import Painting, Tag
from users.models import Profile
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def paginatePaintings(request, paintings, num_per_page):
    page = request.GET.get("page")
    print("page:", page)
    paginator = Paginator(paintings, num_per_page)

    try:
        paintings = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        paintings = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        paintings = paginator.page(page)

    left_index = max(int(page)-3, 1)
    right_index = min(left_index + 4, paginator.num_pages + 1)
    custom_range = range(left_index, right_index)
    return paintings, custom_range

def searchPainting(request):
    
    search_query = ""

    if request.GET.get("search_query"):
        search_query = request.GET.get("search_query")
        
    filter_profiles = Profile.objects.filter(username__icontains=search_query)
    filter_tags = Tag.objects.filter(name__iexact=search_query)
    profiles = Painting.objects.distinct().filter(
        Q(owner__in=filter_profiles) | 
        Q(title__icontains=search_query) |
        Q(tags__in=filter_tags))
    
    return profiles, search_query