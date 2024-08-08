from django.shortcuts import render, redirect
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests

from .forms import BookRecommendationForm
from .models import Book, BookRecommendation, Comment, Like
from .serializers import BookSerializer, BookRecommendationSerializer, CommentSerializer, LikeSerializer

# Constants
API_KEY = 'your_google_books_api_key'
BASE_URL = 'https://www.googleapis.com/books/v1/volumes'

# Function-based Views
def submit_recommendation(request):
    """Handle book recommendation submissions."""
    form = BookRecommendationForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('recommendation_list')
    return render(request, 'submit_recommendation.html', {'form': form})

@api_view(['GET'])
def search_books(request):
    """Search books using Google Books API."""
    query = request.GET.get('query', '')
    params = {'q': query, 'key': API_KEY}
    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        return Response(response.json())
    return Response({'error': 'Failed to fetch data from Google Books API'}, status=response.status_code)

# ViewSets
class BookViewSet(viewsets.ModelViewSet):
    """CRUD operations for Book model."""
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookRecommendationViewSet(viewsets.ModelViewSet):
    """CRUD operations for BookRecommendation model."""
    queryset = BookRecommendation.objects.all()
    serializer_class = BookRecommendationSerializer

class CommentViewSet(viewsets.ModelViewSet):
    """CRUD operations for Comment model."""
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class LikeViewSet(viewsets.ModelViewSet):
    """CRUD operations for Like model."""
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
