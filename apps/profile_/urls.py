from django.urls import path

from apps.profile_.views import ProfileDetailView, ProfileCreateView, ProfileUpdateView, ProfileDeleteView

urlpatterns = [
    path('profile_/<uuid:pk>/', ProfileDetailView.as_view(), name='profile_detail'),
    path('profile_/new/', ProfileCreateView.as_view(), name='profile_new'),
    path('profile_/<uuid:pk>/edit/', ProfileUpdateView.as_view(), name='profile_edit'),
    path('profile_/<uuid:pk>/delete/', ProfileDeleteView.as_view(), name='profile_delete'),
]