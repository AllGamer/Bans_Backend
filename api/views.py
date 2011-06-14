# Create your views here.
from django.http import *
from api.models import *
import datetime

def index(request):
    return HttpResponse("This is the api for the CraftRepo Bans System. This page will link to the documentation later...")

#def heartbeat(request,api_key,players):
def heartbeat(request,api_key):
    try:
        check = Server.objects.get(apikey=api_key)
    except Server.DoesNotExist:
        raise Http404   
    last_known_heartbeat = Server.objects.filter(apikey=api_key).get(last_heartbeat)
    #new_heartbeat = datetime.datetime.now()
    #Server.objects.update(last_heartbeat,new_heartbeat)
    return HttpResponse("Not Yet Implemented")

def unban(request):
    return HttpResponse("Not Yet Implemented")

def ban(request):
    return HttpResponse("Not Yet Implemented")