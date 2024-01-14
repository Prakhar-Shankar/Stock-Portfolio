from django.shortcuts import render

#pk_1d29f40ff033462a8b4783bfae48aa78

def home(request):
    import requests
    import json

    if request.method == "POST":
        ticker = request.POST['ticker']


        api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + ticker + "/quote?token=pk_1d29f40ff033462a8b4783bfae48aa78")

        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error..."

        return render(request, 'home.html', {'api': api})

    else:
        return render(request, 'home.html', {'ticker': "Enter a Ticker Symbol Above..."})

    
    
def about(request):
    return render(request, 'about.html', {})

def add_stock(request):
    return render(request, 'add_stock.html', {})
