from django.urls import path 
from . import views

urlpatterns = [
    path("", views.profiles, name = "profiles"),
    path("profile/<str:pk>", views.userProfile, name="single-profile"),
    path("login/", views.loginUser, name="login-user"),
    path("logout/", views.logoutUser, name="logout-user"),
    path("register/", views.registerUser, name="register"),
    path("account/", views.userAccount, name="account"),
    path("edit-account/", views.editAccount, name="edit-account"),
    path("create-skill/", views.createSkill, name="create-skill"),
    path("edit-skill/<str:pk>", views.editSkill, name="edit-skill"),
    path("delete-skill/<str:pk>", views.deleteSkill, name="delete-skill"),
    path("inbox/", views.inbox, name="inbox"),
    path("message/<str:pk>", views.viewMessage, name="view-message"),
    path("create-message/<str:pk>", views.createMessage, name="create-message"),
]

