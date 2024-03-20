from django.conf import settings
from .models import Profile
from django.contrib.auth.models import User

'''
                            - Signals -
    This will listen on saves or presaves in the application
'''
from django.db.models.signals import post_save ,post_delete
from django.dispatch import receiver
from .models import Profile

from django.core.mail import send_mail

#@receiver(post_save,sender=Profile)
def createProfile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            name=user.first_name,
        )

        subject = 'Welcome To Dev Search Platform'
        message = f'Devsearch Platform Welcomes You. We Hope To start an Awesome Journey with you {profile.username}'
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [profile.email],
            fail_silently=False,
            )

def updateUser(sender, instance , created, **kwargs):
    profile  = instance
    user = profile.user
    if created == False:
        user.first_name = profile.name
        user.username = profile.username
        user.email = profile.email
        user.save()

def deleteUser(sender,instance ,**kwargs):
    try:
        user = instance.user
        user.delete()
    except:
        pass   
    # when profile is deleted we get user and cascade it automatically if not then profile get parent user and delete it using signales.

post_save.connect(createProfile, sender=User)
post_save.connect(updateUser,sender = Profile)
post_delete.connect(deleteUser,sender=Profile)