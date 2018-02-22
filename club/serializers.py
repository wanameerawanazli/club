from django.contrib.auth.models import User
from rest_framework import serializers
from club.models import Club


class ClubSerializer(serializers.HyperlinkedModelSerializer):
    #owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Club
        fields = ('url','id', 'club_name', 'club_description','club_pic')
        read_only_fields = ('date_created', 'date_modified')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    Club = serializers.HyperlinkedRelatedField(
        many=True, view_name='club-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'club')