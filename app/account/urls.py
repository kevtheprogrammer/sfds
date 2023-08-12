from django.urls import path,include
from django.contrib.auth.decorators import login_required

from .views import *
from land.views import *
app_name = 'account'

urlpatterns = [
    path("", AdminIndexView.as_view(),name="index"),
    path("signup/", SignUpView.as_view(),name="signup"),
    path("profile/<int:pk>/", AdminAccountView.as_view(),name="profile"),
    path("profile/<int:pk>/edit/", AdminAccountEditView.as_view(),name="profile-edit"),
    path("profile/<int:pk>/delete/", AdminAccountDeleteView.as_view(),name="profile-delete"),
    
    path("devices/", UserDevices.as_view(),name="devices"),

    path("soil/", SoilDetailView.as_view(),name="soil"),

    
]

 
 