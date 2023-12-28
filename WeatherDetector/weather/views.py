from django.shortcuts import render
import json
import urllib.request

# Create your views here.
def index(request):
    if request.method=='POST':
        city = request.POST['city']
        api_key = '718ab9d8a118ec882898611d3d791fff'
        link = f'http://api.openweathermap.org/data/2.5/weather?q={city}'
        try:
            res = urllib.request.urlopen(f'{link}&appid={api_key}').read()
            json_data = json.loads(res)
            data = {
                'country_code': str(json_data['sys']['country']),
                'coordinate': str(json_data['coord']['lon'])+" "+str(json_data['coord']['lat']),
                'Temperature':str(json_data['main']['temp'])+"K",
                'Pressure':str(json_data['main']['pressure']),
                'Humidity':str(json_data['main']['humidity']),
            }
        except:
            data={
                'country_code': str("No Such Place.")
            }

    else:
        city=''
        data={}

    return render(request, 'index.html', {'city':city, 'data':data})