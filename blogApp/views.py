from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Blog
from .serializers import BlogSerializer

# Create your views here.
class Blogs(APIView):
    def get(self,req):
        blogs = Blog.objects.values()
        serializedObject = BlogSerializer(blogs,many=True)
        return Response(serializedObject.data,status=200)
    def post(self,req):
        serializer = BlogSerializer(data=req.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=201)
        return Response(serializer.data,status=400)

