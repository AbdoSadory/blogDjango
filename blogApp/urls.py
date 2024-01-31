from django.urls import path
from .views import Blogs,Blog_id
urlpatterns = [
    path('blogs/',Blogs.as_view()),
    path('blogs/<int:id>',Blog_id.as_view()),
]
