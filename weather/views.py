# weather/views.py

from django.shortcuts import render
from django.http import request, HttpResponse
import requests

def home(request):
    if request.method == 'POST':
        city = request.POST.get('city')
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid=3a288d40e341b30f67563fbbd8e78726'
        response = requests.get(url)
        data = dict(response.json())

        if response.status_code == 200:
            try:
                return render(request, 'weather.html', {
                    'city': data['name'],
                    'main': data['weather'][0]['main'],
                    'temp': data['main']['temp'],
                    'max': data['main']['temp_max'],
                    'min': data['main']['temp_min'],
                    'feels': data['main']['feels_like'],
                })
            except KeyError:
                error_message = "Error: Weather data for the city not found."
        else:
            error_message = f"Error: City '{city}' not found or API request failed."

        return render(request, 'index.html', {'error': error_message})

    return render(request, 'index.html')
