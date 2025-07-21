from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

# Create your models here.
class user(AbstractUser):
       class role(models.TextChoices):
           GUEST ='GUEST','guest'
           HOST= 'HOST','host'
           ADMIN ='ADMIN','admin'
       phone_number =models.CharField(max_length=20, null=False),
       role = models.CharField(max_length=20,null=False, choices=role.choices)
       created_at = models.TimeField(auto_now= True)


class Conversation(models.Model):
    conversation_id =models.UUIDField(primary_key=True, unique=True)
    
    participants_id = models.ForeignKey(user, on_delete=models.CASCADE)
    created_at = models.TimeField(auto_now= True)

    

class Message(models.Model):

    message_id =models.UUIDField(primary_key=True)
    sender_id =models.ForeignKey(user,on_delete=models.CASCADE)
    message_body =models.TextField(null=False)
    sent_at =models.TimeField(auto_now= True)
    