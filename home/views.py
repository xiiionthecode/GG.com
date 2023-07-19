from django.shortcuts import render

def LandingPage(request):




    meta_title = "Power Of Game"
    meta_descriptions = ""

    contexts = {
        'meta_title' : meta_title,
        'meta_descriptions' : meta_descriptions,
    }

    return render(request, 'home/LandingPage.html', contexts)
