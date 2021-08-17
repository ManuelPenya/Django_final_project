from rest_framework import viewsets, permissions, generics
from .serializers import VideoGameSerializer, \
    UserSerializer, UserProfileSerializer, \
    PartySerializer, PartyMessageSerializer
from .models import VideoGame, UserProfile, Party, PartyMessage

from django.contrib.auth.models import User
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


class PartyMessageViewSet(viewsets.ModelViewSet):
    queryset = PartyMessage.objects.all().order_by('created_at')
    serializer_class = PartyMessageSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class PartyViewSet(viewsets.ModelViewSet):
    queryset = Party.objects.all().order_by('id')
    serializer_class = PartySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class VideoGameViewSet(viewsets.ModelViewSet):
    queryset = VideoGame.objects.all().order_by('id')
    serializer_class = VideoGameSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all().order_by('id')
#     serializer_class = UserSerializer
#     permission_classes = [permissions.IsAuthenticatedOrReadOnly,
#                           IsCorrectUserOrReadOnly]


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