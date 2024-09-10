from django.urls import path

from . import views

app_name = "prof_site_app"
urlpatterns = [
    path("", views.home, name="home"),
    path("Experience/", views.experience, name="experience"),
    path("Blog/", views.blog_list, name="blog_list"),
    path("<str:page_name>/", views.placeholder, name="placeholder"),
]
