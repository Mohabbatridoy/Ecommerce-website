from django.urls import path
from . import views

app_name = "app_login"

urlpatterns = [
    path('signup/', views.sign_up, name="signup"),
    path('login/', views.log_in, name="login"),
    path('logout/', views.log_out, name="logout"),
    path('edit-profile/', views.user_profile, name="edit_profile"),
]