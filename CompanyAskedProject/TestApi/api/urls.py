from django.urls import path
from . import views 

urlpatterns = [
    path("/api/get", views.User_view),
    # path("articles/<int:year>/", views.year_archive),
]