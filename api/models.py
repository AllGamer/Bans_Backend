from django.db import models
from django.db.models import F

# Create your models here.

class Server(models.Model):
    servername = models.CharField(max_length=50)
    apikey = models.CharField(max_length=50)
    last_heartbeat = models.DateTimeField()
    known_server_ip = models.IPAddressField()
    def __unicode__(self):
        return self.servername
    
class User(models.Model):
    username = models.CharField(max_length=15)
    server = models.ForeignKey(Server)
    email = models.EmailField()
    password = models.CharField(max_length=50)
    lastip = models.IPAddressField()
    create_date = models.DateField()
    def __unicode__(self):
        return self.username

class Ban(models.Model):
    username = models.CharField(max_length=15)
    server = models.ForeignKey(Server)
    banned_by = models.ForeignKey(User)
    ban_time = models.DateTimeField()
    banned_ip = models.IPAddressField()
    ban_types = (
    ('G', 'Greifing'),
    ('S', 'Stealing'),
    ('H', 'Hacking'),
    ('I', 'IP Ban'),
    )
    ban_type = models.CharField(max_length=1, choices=ban_types)
    def __unicode__(self):
        return self.username
    def was_pardoned(self):
        if Pardon.ban_id==None:
            return 1==3
        else:
            return 1==1

class Pardon(models.Model):
    ban_id = models.ForeignKey(Ban)
    pardon_time = models.DateTimeField()
    pardoned_by = models.ForeignKey(User)
    pardoned_name = models.CharField(max_length=15)
    def __unicode__(self):
        return self.pardoned_name