from django.shortcuts import render, redirect
from .models import Stock
from .forms import Stockform
from django.contrib import messages


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
    if request.method == 'POST':
        form = Stockform(request.POST or None)

        if form.is_valid():
            form.save()
            messages.success(request, "Stock has been added successfully")
            return redirect('add_stock')
        
    else:
        ticker = Stock.objects.all()
        return render(request, 'add_stock.html', {"ticker": ticker})
