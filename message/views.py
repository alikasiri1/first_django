from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic import ListView   # help to read data base
from .models import Message

# fonctional
def messageView(request):
#     # return HttpResponse('<h2>this is your message<h2>')
    context = {'name':'ali' , 'age' : 180 , 'message_list':Message.objects.all()}
    return render(request , 'home.html' , context)


# objectiv
class MessageView(ListView):
    model = Message
    template_name = 'home.html'
    context_object_name = 'your_objects'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['message_list'] = Message.objects.all()  # Add this line to include message_list
        context['name'] = 'Ali'
        context['age'] = 18
        
        return context