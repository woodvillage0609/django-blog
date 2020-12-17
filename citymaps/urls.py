from django.urls import path
from . import views


urlpatterns = [
	path('citymaps', views.CityListView.as_view(), name='citymaps-index'),
    path('citymaps/<int:pk>', views.CityDetailView.as_view(), name='citymaps-detail'),
]