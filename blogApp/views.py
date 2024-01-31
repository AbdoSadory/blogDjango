from django.http import Http404
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


class Blog_id(APIView):

    def get_object(self,id):
        try:
            return Blog.objects.get(pk=id)
        except Blog.DoesNotExist:
            raise Http404
        
    def get(self,request,id):
        blog = self.get_object(id)
        serializedObject = BlogSerializer(blog)
        return Response(serializedObject.data,status=200)
    
    def put(self,request,id):
        blog = self.get_object(id)
        serializer = BlogSerializer(blog,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=200)
        return Response(serializer.data,status=400)

    def delete(self,request,id):
        blog= self.get_object(id)
        blog.delete()
        return Response({"message":"Deleted successfully"},status=200)