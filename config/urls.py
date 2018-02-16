from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name="base/landing.html"), name="landing"),
    path('api/users/', include("apps.users.urls", namespace="api-users")),
    path('api/balances/', include("apps.balance.urls", namespace="api-balances")),
]
