from django.http import HttpResponse

from django.shortcuts import render
from django.core.cache import cache


def home(request):
    
    context = {'title': 'Portfolio','name':'Renjith','':'','':'','':'','':'','':'','':'','':'','':'','':'','':'','':'','':'','':'','':'','':'','':'','':'','':''}
    return render(request, '1dis.html', context)
def index(request):
    
    context = {'title': 'Portfolio','name':'Renjith','':'','':'','':'','':'','':'','':'','':'','':'','':'','':'','':'','':'','':'','':'','':'','':'','':'','':''}
    return render(request, 'hero.html', context)
def hero(request):
    
    context = {'title': 'Portfolio','name':'Renjith','':'','':'','':'','':'','':'','':'','':'','':'','':'','':'','':'','':'','':'','':'','':'','':'','':'','':''}
    return render(request, 'hero.html', context) 

def about(request):
    
    context = {'title': 'Portfolio','name':'Renjith','':'','':'','':'','':'','':'','':'','':'','':'','':'','':'','':'','':'','':'','':'','':'','':'','':'','':''}
    return render(request, 'about.html', context)
def resume(request):
    
    context = {'title': 'Portfolio','name':'Renjith','':'','':'','':'','':'','':'','':'','':'','':'','':'','':'','':'','':'','':'','':'','':'','':'','':'','':''}
    return render(request, 'resume.html', context)
def portfolio(request):
    
    context = {'title': 'Portfolio','name':'Renjith','':'','':'','':'','':'','':'','':'','':'','':'','':'','':'','':'','':'','':'','':'','':'','':'','':'','':''}
    return render(request, 'portfolio.html', context)
def service(request):
    
    context = {'title': 'Portfolio','name':'Renjith','':'','':'','':'','':'','':'','':'','':'','':'','':'','':'','':'','':'','':'','':'','':'','':'','':'','':''}
    return render(request, 'service.html', context)
def contact(request):
    
    context = {'title': 'Portfolio','name':'Renjith','':'','':'','':'','':'','':'','':'','':'','':'','':'','':'','':'','':'','':'','':'','':'','':'','':'','':''}
    return render(request, 'contact.html', context)
