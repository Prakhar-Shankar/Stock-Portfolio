from django.shortcuts import render

#pk_1d29f40ff033462a8b4783bfae48aa78

def home(request):
    return render(request, 'home.html', {})
    
def about(request):
    return render(request, 'about.html', {})
