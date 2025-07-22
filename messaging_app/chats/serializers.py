from rest_framework import serializers
from .models import User,Message,Conversation

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =['user_id','first_name','last_name','email','password_hash','phone_number','role','created_at']
          
    

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
       model = Message
       fields =['message_id','sender_id', 'message_body', 'sent_at']

   


class ConversationSerializer(serializers.ModelSerializer):

       class Meta:
           model =Conversation['participants_id','created_at']

       pass