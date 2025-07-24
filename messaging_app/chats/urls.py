from django.urls import path

from . import views

urlpatterns =[
             path("", views.ConversationViewSet, name="conversation"),
             path("", views.MessageViewSet, name="Message"),

             ]      