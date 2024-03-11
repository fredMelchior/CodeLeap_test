from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import PostModel, UserModel
from .serializers import PostSerializer, UserSerializer


# User Viewset:
class UserViewset(viewsets.ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer

    # Create user/username
    def create_user(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


# Posts Viewset
class PostViewset(viewsets.ModelViewSet):
    queryset = PostModel.objects.all()
    serializer_class = PostSerializer

    # Create post
    def create_post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Get all posts
    def list_posts(self, request):
        serializer = PostSerializer(self.queryset, many=True)
        return Response(serializer.data)

    # Edit posts
    def edit_post(self, request, pk=None):
        post = PostModel.objects.get(pk=pk)
        serializer = self.serializer_class(post, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    # Delete posts
    def delete_post(self, request, pk=None):
        post = PostModel.objects.get(pk=pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
