from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

# def messageView(request):
#     # return HttpResponse('<h2>this is your message<h2>')
#     return render(request , 'home.html')

class messageView(TemplateView):
    template_name = 'home.html'