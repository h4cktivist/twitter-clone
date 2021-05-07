from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import PostSerializer

from main.models import Post


@api_view(['GET'])
def apiOverview(request):
    api_endpoints = {
        'List': '/posts/',
        'Detail': '/posts/{id}/',
    }

    return Response(api_endpoints)


@api_view(['GET'])
def postsList(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def postDetail(request, id):
    try:
        post = Post.objects.get(id=id)
        serializer = PostSerializer(post, many=False)
    
        return Response(serializer.data)

    except:
        return Response('Requested Post Does Not Exist')
