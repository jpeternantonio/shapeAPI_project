from rest_framework import generics
from .serializers import ShapeSerializer, UserSerializer
from rest_framework import permissions, parsers, viewsets
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from ..models import *
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.hashers import make_password


class ShapeListView(generics.ListAPIView):
    queryset = Shape.objects.all()
    
    serializer_class = ShapeSerializer
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]


class ShapeAddView(APIView):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)
    parser_classes = (parsers.JSONParser,)
   

    def post(self, request, format=None):
        name = request.data['name']
        side = request.data['side']
        height = request.data['height']
        base = request.data['base']
        shape = Shape(name=name, side=side, height=height, base=base)
        shape.save()
        return Response('created')

    def delete(self, request, format=None):
        name = request.data['name']
        shape = Shape.objects.get(name=name)
        shape.delete()
        return Response('deleted')

    def put(self, request, format=None):
        name = request.data['name']
        side = request.data['side']
        height = request.data['height']
        base = request.data['base']
        shape = Shape.objects.get(name=name)
        shape.side = side
        shape.height = height
        shape.base = base
        shape.save()
        return Response('updated')


class UserAddView(APIView):
    parser_classes = (parsers.JSONParser,)
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        username = request.data['username']
        email = request.data['email']
        password = request.data['password']
        user = User(username=username, email=email, password=make_password(password), is_superuser=True, is_staff=True)
        user.save()
        return Response(UserSerializer(user).data)


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)

class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

