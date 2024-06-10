from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("", views.getRoutes),
    path("paintings/", views.getPaintings),
    path('paintings/<str:pk>', views.getPainting),
    path('paintings/<str:pk>/vote/', views.paintingVote),
    path('remove-tag/', views.removeTag),

    path('users/token/', TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('users/token/refresh/', TokenRefreshView.as_view(),name='token_refresh'),

]