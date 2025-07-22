from rest_framework import serializers
from .models import User,Message,Conversation

class UserSerializer(serializers.ModelSerializer):
    last_name = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields =['user_id','first_name','last_name','email','password_hash','phone_number','role','created_at']
          
    

class MessageSerializer(serializers.ModelSerializer):

    message_body = serializers.CharField()

    class Meta:
       model = Message
       fields =['message_id','sender_id', 'message_body', 'sent_at']

   


class ConversationSerializer(serializers.ModelSerializer):

       class Meta:
           
           model  = Conversation
           fields = ['participants_id','created_at']

           def validate_content(self, value):
               if not value.strip():
                   raise serializers.ValidationError("participants_id cannot be empty.")
               
               

       