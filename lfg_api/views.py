from rest_framework import viewsets, permissions, generics
from .serializers import VideoGameSerializer, \
    UserSerializer, UserProfileSerializer, \
    PartySerializer, PartyMessageSerializer
from .models import VideoGame, UserProfile, Party, PartyMessage

from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from lfg_api.permissions import IsOwnerOrReadOnly, IsCorrectUserOrReadOnly


# Create your views here.
@api_view(["GET"])
@csrf_exempt
@permission_classes([IsAuthenticated])
def welcome(request):
    content = {"message": "Welcome to your Video Store"}
    return JsonResponse(content)


class PartyMessageList(generics.ListCreateAPIView):
    """
    List and create for party messages, showed at "/parties/<id>/messages"
    """
    serializer_class = PartyMessageSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get_queryset(self, **kwargs):
        """
        This view should return a list of all messages from the current party
        """
        party_id = self.kwargs['party_id']
        return PartyMessage.objects.filter(party__id=party_id)

    def perform_create(self, serializer, **kwargs):
        """
        Saving Party messages with owner as current user and party as current
        party in URL.
        """
        party_id = self.kwargs['party_id']
        party = Party.objects.get(pk=party_id)
        serializer.save(owner=self.request.user, party=party)


class PartyMessageDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    View to show party messages for an specific party group.
    Url established as /parties/<party_id>/messages/ (see urls.py)
    """
    serializer_class = PartyMessageSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def get_queryset(self, **kwargs):
        """
        This view should return a list of all messages from the current party
        """
        party_id = self.kwargs['party_id']
        return PartyMessage.objects.filter(party__id=party_id)


class PartyViewSet(viewsets.ModelViewSet):
    """
    Parties view that includes a filtering method to search for parties
    given a video_game.
    Search url as /parties?video_game=????/
    """

    queryset = Party.objects.all().order_by('id')
    serializer_class = PartySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['video_game']

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class VideoGameViewSet(viewsets.ModelViewSet):
    queryset = VideoGame.objects.all().order_by('id')
    serializer_class = VideoGameSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserList(generics.ListAPIView):
    """
    List view to display all users but only in list mode
    """
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer


class UserProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Generic user profile view to modify special characteristics for app users,
    such as `social_network_link` or `steam_user`
    """
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsCorrectUserOrReadOnly]
