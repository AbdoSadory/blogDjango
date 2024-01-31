from django.urls import path
from .views import Blogs,Blog_id,Writers,Writer_id
urlpatterns = [
    path('blogs/',Blogs.as_view()),
    path('blogs/<int:id>',Blog_id.as_view()),
    path('writers/',Writers.as_view()),
    path('writers/<int:id>',Writer_id.as_view()),
]
