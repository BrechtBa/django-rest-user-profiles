from django.db import models
from django.contrib.auth.models import User, Group
from django.db.models.signals import post_save


# model definition
class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile', blank=True, null=True)
	displayname = models.CharField(max_length=100, blank=True, default='')
	avatar = models.CharField(max_length=256, blank=True, default='')

class AvatarUpload(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='avatar_upload', blank=True, null=True)
	file = models.FileField(upload_to='avatars/', blank=True, default='')



def prepare_user(sender, **kwargs):
	"""
	performs actions new user is created
	"""

	user = kwargs['instance']
	if kwargs['created']:
		# create the user profile
		try:
			user.profile
		except:
			user_profile = UserProfile(user=user,displayname=user.username)
			user_profile.save()
		
		# create the avatar upload
		try:
			user.avatar_upload
		except:
			avatar_upload = AvatarUpload(user=user)
			avatar_upload.save()
			
post_save.connect(prepare_user, sender=User)
