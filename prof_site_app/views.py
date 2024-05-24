from django.shortcuts import render

from .models import HomePage


def home(request):
    home_page_info = HomePage.objects.get(pk=1)
    context = {
        "home_page_info": home_page_info
    }
    return render(request, "prof_site_app/home.html", context)


def placeholder(request, page_name: str):
    page_name = page_name.capitalize()
    if page_name == "Experience" or page_name == "Projects" or page_name == "Blog" or page_name == "Passions":
        context = {
            "image_link": 'prof_site_app/images/{}.jpg'.format(page_name.lower()),
            "page_name": page_name
        }
    else:
        context = {
            "error_message": "Page does not exist for : {}".format(page_name)
        }
    return render(request, "prof_site_app/placeholder.html", context)
