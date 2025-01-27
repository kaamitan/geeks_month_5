# from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("director/", views.DirectorListAPIView.as_view(), name="director-list"),
    path(
        "director/<int:pk>",
        views.DirectroDetailAPIView.as_view(),
        name="director-detail",
    ),
    path("movie/", views.MovieListAPIView.as_view(), name="movie-list"),
    path("movie/<int:pk>", views.MovieDetailAPIView.as_view(), name="movie-detail"),
    path("review/", views.ReviewListAPIView.as_view(), name="review-list"),
    path(
        "review/<int:pk>",
        views.ReviewDetailAPIView.as_view(),
        name="review-detail",
    ),
]
