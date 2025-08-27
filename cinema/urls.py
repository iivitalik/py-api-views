from django.urls import path, include
from .views import (
    GenreAPIView,
    GenreDetailAPIView,
    ActorListCreateView,
    ActorDetailView,
    CinemaHallViewSet,
    router
)

app_name = "cinema"

urlpatterns = [
    path("genres/", GenreAPIView.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreDetailAPIView.as_view(), name="genre-detail"),
    path("actors/", ActorListCreateView.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorDetailView.as_view(), name="actor-detail"),
    path("cinema_halls/", CinemaHallViewSet.as_view(
        {"get": "list", "post": "create"}), name="cinema-hall-list"),
    path("cinema_halls/<int:pk>/", CinemaHallViewSet.as_view({
        "get": "retrieve",
        "put": "update",
        "patch": "partial_update",
        "delete": "destroy"
    }), name="cinema-hall-detail"),
    path("", include(router.urls)),
]
