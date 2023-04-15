
from django.shortcuts import render
from .models import journels
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from django.urls import reverse_lazy
def index(request):
    
    context = {'title': 'Portfolio',}
    return render(request, '1dis.html', context)

class JournelCreateView(CreateView):
    model = journels
    fields =['Products','amount','Invoice','Date']
    template_name = "journel/create.html"
    success_url =reverse_lazy('listjournel')


class JournelListView(ListView):
      model = journels
      template_name = "journel/list.html"
      