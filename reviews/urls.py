from django.urls import path
from . import views

urlpatterns = [
    path('', views.ReviewView.as_view()),
    path('thank-you', views.ThankYou.as_view()),
    path("reviews", views.ReviewList.as_view()),
    path("reviews/favorite",views.AddFavoriteView.as_view()),
    path("reviews/<int:pk>", views.SingleReview.as_view())
]