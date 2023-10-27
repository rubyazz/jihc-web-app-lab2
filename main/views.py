# views.py
from django.shortcuts import render
import requests

def home(request):
    country = request.GET.get('country', 'France')  # Default country is set to France
    url = "https://covid-193.p.rapidapi.com/statistics"
    querystring = {"country": country}
    headers = {
        'x-rapidapi-key': "d7af63a666mshc3f4a24426ace55p14ea0cjsn2e3c9e8fe3d9",
        'x-rapidapi-host': "covid-193.p.rapidapi.com"
    }
    response = requests.request("GET", url, headers=headers, params=querystring).json()

    if 'response' in response:
        data = response['response']
        d = data[0]
        context = {
            'country': d['country'],
            'all': d['cases']['total'],
            'recovered': d['cases']['recovered'],
            'deaths': d['deaths']['total'],
            'new': d['cases']['new'],
            'critical': d['cases']['critical'],
            'date': d['day']
        }
        return render(request, 'index.html', context)
    else:
        error_message = "Data not available at the moment. Please try again later."
        return render(request, 'error.html', {'error_message': error_message})
