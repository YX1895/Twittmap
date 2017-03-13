from django.shortcuts import render
from django.http import HttpResponse, request, JsonResponse
# from .forms import MyForm
import requests
import json

# Create your views here.


def Index(Request):
    return render(Request, 'googleMap/map.html')



def Post(Request):
    if Request.method == "POST":
        msg = Request.POST.get('Search', None)

        host = 'https://search-twittermap-inuckwupgoy3q4rf7vxtv65y5y.us-west-1.es.amazonaws.com/twittermap/_search?q='

        url = host + msg
        response = requests.get(url)
        r = json.loads(response.text)
        tweet = [res['_source']['tweet'] for res in r['hits']['hits']]
        data = [res['_source']['coordinates'] for res in r['hits']['hits']]
        print tweet
        hits = len(data)
        length = {'hits': hits}
        coordinates = {}
        tweets = {}
        for i in range(hits):
            if (data[i][0] < - 90):
                data[i][0] = data[i][0] + 180
            coordinates[i] = {'lat': data[i][1], 'lng': data[i][0]}
            tweets[i] = {'tweet': tweet[i]}

        data = {'coordinates': coordinates, 'length': length,'tweets': tweets}

        return JsonResponse(data)