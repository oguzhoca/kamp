from datetime import date
from django.shortcuts import render
from django.views import View
from .models import Client 
from django.views.generic import DetailView

def client_view(request):  
    clients = Client.objects.all().order_by('-date')

    context = {
        'clients': clients
    }

    return render(request, 'client.html', context)

class ClientDetailView(DetailView):
    model = Client
    template_name = 'client_detail.html' 
    context_object_name = 'client' 


class ClientDateView(View):
    template_name = 'client_list.html'

    def get(self, request, date):
        clients = Client.objects.filter(date=date)
        context = {
            'selected_date': date,
            'clients': clients,
        }
        return render(request, self.template_name, context)
    



class BlogDateView(View):
    template_name = 'client_list.html'

    def get(self, request, date):
        clients = Client.objects.filter(date=date)
        context = {
            'selected_date': date,
            'clients': clients,
        }
        return render(request, self.template_name, context)
