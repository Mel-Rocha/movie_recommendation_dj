from django.urls import path

from . import views
from apps.home.views import CustomLoginView

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', CustomLoginView.as_view(), name='login'),

]
