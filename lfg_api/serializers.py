from rest_framework import serializers
from django.contrib.auth.models import User

from .models import VideoGame, UserProfile, Party, PartyMessage


class PartyMessageSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    party = serializers.ReadOnlyField(source='party.name')

    class Meta:
        model = PartyMessage
        fields = ('id',
                  # 'url',
                  'message',
                  'owner',
                  'party',
                  'created_at'
                  )


class PartySerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    # TODO: not sure if I can get the linked relationship working
    # party_messages = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     view_name='partymessage-detail',
    #     read_only=True
    # )

    class Meta:
        model = Party
        fields = ('id',
                  'url',
                  'name',
                  'image',
                  'description',
                  'video_game',
                  'owner',
                  # 'party_messages'
                  )


class VideoGameSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    parties = serializers.HyperlinkedRelatedField(
        many=True,
        view_name='party-detail',
        read_only=True
    )

    class Meta:
        model = VideoGame
        fields = ('id',
                  'url',
                  'title',
                  'image',
                  'type_of_game',
                  'play_time',
                  'owner',
                  'parties')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    parties = serializers.HyperlinkedRelatedField(
        many=True,
        view_name='party-detail',
        read_only=True)
    videogames = serializers.HyperlinkedRelatedField(
        many=True,
        view_name='videogame-detail',
        read_only=True)

    class Meta:
        model = User
        fields = ('id',
                  'username',
                  'email',
                  'videogames',
                  'parties',
                  )


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('user_id',
                  'social_network_link',
                  'steam_user',
                  )
