from django.shortcuts import render
import requests, json

def home(request):
    url = "https://covid-193.p.rapidapi.com/statistics"

    querystring = {"country":"France"}

    headers = {
        'x-rapidapi-key': "a6f5f5daa9msh415e131fbb7e735p1994d1jsnb2bc491b075e",
        'x-rapidapi-host': "covid-193.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring).json()

    data = response['response']

    d = data[0]

    print(d)

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
