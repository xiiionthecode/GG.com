from django.shortcuts import render
from config.tracker import get_ip_address
from settings.models import Generally
from settings.models import LandingPage as LandingPageModel

def LandingPage(request):
    logo = ""
    icon = ""
    meta_title = ""
    meta_descriptions =" "


    generally_obj = Generally.objects.none()
    landingpage_obj = LandingPageModel.objects.none()
    

    if Generally.objects.filter(active=True).exists():
        generally_obj = Generally.objects.get(active=True)
        logo = generally_obj.logo
        icon = generally_obj.icon

    if LandingPageModel.objects.filter(active=True).exists():
        landingpage_obj = LandingPageModel.objects.get(active=True)
        meta_title = landingpage_obj.meta_title
        meta_descriptions = landingpage_obj.meta_descriptions


    # Client Ip For Cockies
    client_ip = get_ip_address(request)

    contexts = {
        'logo' : logo,
        'icon' : icon,
        'meta_title' : meta_title,
        'meta_descriptions' : meta_descriptions,
    }

    return render(request, 'home/LandingPage.html', contexts)
