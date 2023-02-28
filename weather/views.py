from django.shortcuts import render
import requests


# Create your views here.


def weather_data(city):
    if not city:
        return {}
    weather_api = '6572e5f4611648219fc143140232702'
    request_url = f'http://api.weatherapi.com/v1/current.json?key={weather_api}&q={city}&aqi=no'
    res = requests.get(request_url)
    data = res.json()
    if data.get('error'):
        results = {}
    else:
        results = {'city_name': data.get('location').get('name'), 'country_name': data.get('location').get('country'),
                   'weather_condition': data.get('current').get('condition').get('text'),
                   'temperature': data.get('current').get('temp_c'), 'date': data.get('location').get('localtime')}

    return results


def home_view(request):
    if request.method == 'GET' and 'city' in request.GET:
        city = request.GET.get('city')
        results = weather_data(city)
        context = {'results': results}
    else:
        context = {}
    return render(request, 'home.html', context)
