from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def events(request):
    return render(request, 'events.html')

def blog(request):
    return render(request, 'blog.html')

def past_events(request):
    return render(request, 'pastevents.html')

def contact(request):
    return render(request, 'contact.html')

def support(request):
    return render(request, 'support.html')