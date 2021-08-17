from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'videogames', views.VideoGameViewSet)
router.register(r'parties', views.PartyViewSet)
router.register(r'party_messages', views.PartyMessageViewSet)
# router.register(r'users', views.UserViewSet)

# Wire up oru API using automatic URL routing
urlpatterns = [
    path('', include(router.urls)),
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserProfileDetail.as_view(),
         name='userprofile-detail'),
    path('api-auth/', include('rest_framework.urls',
                              namespace='rest_framework')),
    path('api/welcome/', views.welcome),
]
