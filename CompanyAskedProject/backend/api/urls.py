from django.urls import path
# from .views import MovieCreateView ,MovieDetailView ,MovieListCreateAPIView
from .views import MovieDetailAPIView ,AddReviewAPIView,DeleteReviewAPIView ,MovieListCreateAPIView


# urlpatterns = [
#     # path('', home),
#     path('movies/', MovieCreateView.as_view(), name = 'movie' )
# ]

# urlpatterns = [
#     path('movies/', MovieCreateView.as_view(), name='movie-list-create'),
#     path('movies/<int:pk>/', MovieDetailView.as_view(), name='movie-detail'),
# ]

urlpatterns = [
    path('movies/', MovieListCreateAPIView.as_view(), name='movie-list-create'),
    path('movies/<int:pk>/', MovieDetailAPIView.as_view(), name='movie-detail'),
    path('movies/<int:pk>/add-review/', AddReviewAPIView.as_view(), name='add-review'),
    path('movies/<int:pk>/delete-review/<int:review_id>/', DeleteReviewAPIView.as_view(), name='delete-review'),
]
