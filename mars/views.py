import requests
from django.shortcuts import render


def home(request):
    return render(request, 'home.html')


def get_mars_photo(request, rover_name):
    API_KEY = 'UYx0qe9h2Xc1U1e2yNFFoHsOQsgv6SbiWZGfheVB'
    rovers = ['perseverance', 'curiosity', 'spirit', 'opportunity']
    if rover_name in rovers:
        response = requests.get(
            f"https://api.nasa.gov/mars-photos/api/v1/rovers/{rover_name}/latest_photos?api_key={API_KEY}").json()
        photos = response.get('latest_photos')

        context = {
            'photos': photos
        }
        return render(request, 'rovers.html', context)
    else:
        context = {
            'error': f'Rover:{rover_name} doesnt exist!'
        }
        return render(request, 'home.html', context)
