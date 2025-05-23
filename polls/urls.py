from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("selected/<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("selected/<int:pk>/results", views.ResultsView.as_view(), name="results"),
    path("selected/<int:question_id>/vote", views.vote, name="vote"),
]