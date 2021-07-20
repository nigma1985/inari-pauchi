from django.urls import path
# from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView
from . import views

urlpatterns = [
    path('', views.home, name='base-home'),
    # path('', PostListView.as_view(), name='home'),
    # path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('impressum/', views.impressum, name='impressum'),
    path('disclaimer/', views.disclaimer, name='disclaimer'),
    path('about/', views.about, name='about'),
]
