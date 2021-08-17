from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE)
    social_network_link = models.CharField(
        max_length=100,
        blank=True)
    steam_user = models.CharField(
        max_length=100,
        blank=True)


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
    else:
        instance.userprofile.save()


class VideoGame(models.Model):

    class TypeOfGame(models.TextChoices):
        ACTION = 'AC', _('Action'),
        ARCADE = 'AR', _('Arcade'),
        PLATFORM = 'PL', _('Platform'),
        SHOOTER = 'SH', _('Shooter'),
        ADVENTURE = 'AD', _('Adventure'),
        SPORT = 'SP', _('Sport'),
        CARS = 'CA', _('Cars'),
        STRATEGY = 'ST', _('Strategy'),
        SIMULATION = 'SI', _('Simulation'),

    title = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=400)
    image = models.CharField(max_length=200)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              related_name='videogames',
                              on_delete=models.CASCADE)
    play_time = models.DecimalField(max_digits=4, decimal_places=1)
    type_of_game = models.CharField(
        max_length=2,
        choices=TypeOfGame.choices,
        default=TypeOfGame.ACTION,
    )

    def __str__(self):
        return self.title


class Party(models.Model):

    name = models.CharField(max_length=100)
    description = models.CharField(max_length=400)
    image = models.CharField(max_length=200)
    video_game = models.ForeignKey(VideoGame,
                                   related_name='parties',
                                   on_delete=models.CASCADE)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              related_name='parties',
                              on_delete=models.CASCADE)

    class Meta:
        app_label = 'lfg_api'

    def __str__(self):
        return self.name


class PartyMessage(models.Model):

    message = models.CharField(max_length=400)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL,
                              related_name='party_messages',
                              on_delete=models.CASCADE)
    party = models.ForeignKey(Party,
                              related_name='party_messages',
                              on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
