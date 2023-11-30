from django.shortcuts import render

def index(request):
    return render(request, 'boton_page.html')
