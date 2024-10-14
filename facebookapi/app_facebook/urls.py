from django.urls import path
from .views import FacebookPostsView

urlpatterns = [
    path('facebook/posts/', FacebookPostsView.as_view(), name='facebook-posts'),
    
]
