from django.shortcuts import render
from rest_framework import generics,permissions
from .serializers import NewsSerializer
from .models import NewsModel
from .permissions import IsAuthorOrNot
# Create your views here.

class NewsListView(generics.ListCreateAPIView):
    queryset = NewsModel.objects.all()
    serializer_class = NewsSerializer

class NewsDetailView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticated & IsAuthorOrNot]
    queryset = NewsModel.objects.all()
    serializer_class = NewsSerializer