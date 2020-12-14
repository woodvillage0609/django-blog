from django.urls import path
from . import views


urlpatterns = [
	path('', views.BlogListView.as_view(), name='blog-home'),
    path('blog/new/', views.BlogCreateView.as_view(), name = 'blog-create'), 
    path('blog/<int:pk>', views.BlogDetailView.as_view(), name='blog-detail'),
    path('blog/<int:pk>/update/', views.BlogUpdateView.as_view(), name ='blog-update'),
    path('blog/<int:pk>/delete/', views.BlogDeleteView.as_view(), name = 'blog-delete'), 
    path('blog/category/<str:category>/', views.CategoryView.as_view(), name='blog-category'),
    path('blog/tag/<str:tag>/', views.TagView.as_view(),name='blog-tag'),
]