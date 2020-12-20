from django.urls import path
from . import views


urlpatterns = [
	path('citymaps', views.CityListView.as_view(), name='citymap-index'),
    path('citymaps/<int:pk>', views.CityDetailView.as_view(), name='citymap-detail'),
    path('citymaps/new', views.CityCreateView.as_view(), name='citymap-create'), 
    path('citymaps/<int:pk>/update', views.CityUpdateView.as_view(), name='citymap-update'),
    path('citymaps/<int:pk>/delete', views.CityDeleteView.as_view(), name='citymap-delete'),
]