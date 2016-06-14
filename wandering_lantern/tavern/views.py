from django.shortcuts import render

# Create your views here.
from .models import Character

def tavern_index(request):
    characters = Character.objects.all()
    templ = loader.get_template('tavern/characters.html')

    context = {'films': films}

    return HttpResponse(templ.render(context, request))
