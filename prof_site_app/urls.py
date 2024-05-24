from django.urls import path

from . import views

app_name = "prof_site_app"
urlpatterns = [
    path("", views.home, name="home"),
    path("<str:page_name>/", views.placeholder, name="placeholder")
]
