from django.shortcuts import render
from rest_framework import viewsets
from .models import Conversation,Message
from .serializers import ConversationSerializer,MessageSerializer
from rest_framework import response

# Create your views here.

class ConversationViewSet(viewsets.ModelViewSet):

    def listConversation(self ,request):
    
          queryset=Conversation.objects.all().filter()
          serializer = ConversationSerializer(queryset, many=True)
          return  response(serializer.data)
    


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all().filter()
    serializer_class = MessageSerializer  
      
