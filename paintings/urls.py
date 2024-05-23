from django.urls import path
from . import views

urlpatterns = [
    path("", views.paintings, name="paintings"),
    path("paintings/<str:pk>/", views.painting, name="painting"),
    path("new-painting", views.createPainting, name="new-painting"),
    path("update-painting/<str:pk>/", views.updatePainting, name="update-painting"),
    path("delete-painting/<str:pk>/", views.deletePainting, name="delete-painting"),
]