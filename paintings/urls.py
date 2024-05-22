from django.urls import path
from . import views

urlpatterns = [
    path("", views.paintings, name="paintings"),
    path("paintings/<str:pk>/", views.painting, name="painting"),
]