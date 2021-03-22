from django.shortcuts import render

def home(request):
    return render(request, 'dist_search/home.html')
