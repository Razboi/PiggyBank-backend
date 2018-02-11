from django.urls import path
from .views import UsersRUDView, UsersCreateView
from rest_framework.authtoken import views

app_name = "users"

urlpatterns = [
    path("<int:pk>", UsersRUDView.as_view(), name="users-rud"),
    path("", UsersCreateView.as_view(), name="users-create"),
    path("token-auth", views.obtain_auth_token)
]
