from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from .serializers import NewsFeedSerializer, SourceSerializer
from rest_framework import generics, mixins, permissions, authentication, status
from .models import NewsFeed, Source


class NewsFeedListCreateAPIView(generics.ListCreateAPIView):
    queryset = NewsFeed.objects.all()
    serializer_class = NewsFeedSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"request": self.request})
        return context
    
news_feed_api_view = NewsFeedListCreateAPIView.as_view()  



class SourceListAPIView(generics.ListAPIView):
    queryset = Source.objects.all()
    serializer_class = SourceSerializer
    permission_classes = [permissions.IsAuthenticated]

source_list_api_view = SourceListAPIView.as_view()
