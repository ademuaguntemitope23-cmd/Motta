import requests
from django.shortcuts import render

def social_apps(request):
    url = "https://motta-c1d5e-default-rtdb.firebaseio.com/apps.json"
    response = requests.get(url)
    data = response.json()

    return render(request, "index.html", {"apps": data})
