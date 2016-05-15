from django.contrib.auth.models import User, Group

from rest_framework import serializers

from rest_user_profiles.models import UserProfile


class RegisterSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('username','email','password')

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = ('id','username','email','groups')

class UserProfileSerializer(serializers.ModelSerializer):
	class Meta:
		model = UserProfile
		
