from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home_page(request):
    # render will seach for home.html from templates directory in any apps directory
    # Then it builds a HttpResponse based on the content of the templates
    return render(request, 'home.html')
