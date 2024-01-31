from django.urls import path
from .views import Blogs
urlpatterns = [
    path('blogs/<int:id>',Blogs.as_view()),
    path('blogs/',Blogs.as_view()),
]
