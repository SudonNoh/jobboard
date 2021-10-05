from django.urls import path
from job.api.views import JobOfferDetailAPIView, JobOfferListCreateAPIView

urlpatterns = [
    path('jobs/', JobOfferListCreateAPIView.as_view(), name='jobs-list'),
    path('jobs/<int:pk>/', JobOfferDetailAPIView.as_view(), name='jobs-detail'),
]