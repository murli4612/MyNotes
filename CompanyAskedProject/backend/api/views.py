from rest_framework import status
from rest_framework.response import Response
from .serializers import MovieSerializer ,ReviewSerializer
from .models import Movie ,Review
from rest_framework.views import  APIView
from rest_framework import  status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404


class MovieListCreateAPIView(APIView):
    def get(self, request):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MovieDetailAPIView(APIView):
    def get(self, request, pk):
        movie = get_object_or_404(Movie, pk=pk)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)
    
    def put(self, request, pk):
        movie = get_object_or_404(Movie, pk=pk)
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        movie = get_object_or_404(Movie, pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class AddReviewAPIView(APIView):
    def post(self, request,pk):
        try:
            movie = Movie.objects.get(id=pk)  # Ensure the movie exists
            print(movie.id, "Movie ID")  # Print the movie ID

        except Movie.DoesNotExist:
            return Response({"error": "Movie not found"}, status=status.HTTP_404_NOT_FOUND)
        data = request.data.copy()
        data['movie'] = movie.id
        serializer = ReviewSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteReviewAPIView(APIView):
    def get(self, request, pk):
        """Retrieve all reviews for a specific movie"""
        movie = get_object_or_404(Movie, pk=pk)
        reviews = Review.objects.filter(movie=movie)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def delete(self, request, pk, review_id):
        movie = get_object_or_404(Movie, pk=pk)
        review = get_object_or_404(Review, pk=review_id, movie=movie)
        review.delete()
        return Response({'message': 'Review deleted'}, status=status.HTTP_204_NO_CONTENT)