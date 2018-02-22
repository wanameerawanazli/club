from django.contrib.auth.models import User
from rest_framework import generics, permissions, renderers, viewsets
from rest_framework.decorators import api_view, detail_route
from rest_framework.response import Response
from rest_framework.reverse import reverse
from club.models import Club
from club.permissions import IsOwnerOrReadOnly
from club.serializers import ClubSerializer, UserSerializer


class ClubViewSet(viewsets.ModelViewSet):
    queryset = Club.objects.all()
    serializer_class = ClubSerializer
    #permission_classes = (
        #permissions.IsAuthenticatedOrReadOnly,
        #IsOwnerOrReadOnly, )
    def create(self, validated_data):
        print(validated_data)
        obj = Club.objects.create(**validated_data)
        return obj

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer