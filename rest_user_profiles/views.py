from django.contrib.auth.models import User, Group
from django.conf import settings

from rest_framework import generics
from rest_framework import filters
from rest_framework import permissions
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from rest_framework.views import APIView

from rest_user_profiles.models import UserProfile,AvatarUpload
from rest_user_profiles.serializers import *
from rest_user_profiles.permissions import *
	
		

# register
class Register(generics.CreateAPIView):
	serializer_class = RegisterSerializer
	permission_classes = (permissions.IsAdminUser,)
	queryset = User.objects.all()

# users
class UserList(generics.ListCreateAPIView):
	serializer_class = UserSerializer
	permission_classes = (permissions.IsAdminUser,)
	queryset = User.objects.all()
	filter_fields = ('groups',)
		
class UserDetail(generics.RetrieveUpdateDestroyAPIView):
	serializer_class = UserSerializer
	permission_classes = (IsOwnerOrAdmin,)
	queryset = User.objects.all()
	
# user profiles	
class UserProfileList(generics.ListCreateAPIView):
	serializer_class = UserProfileSerializer
	permission_classes = (IsAdminOrReadOnly,)
	queryset = UserProfile.objects.all()
	filter_fields = ('user','displayname',)
		
class UserProfileDetail(generics.RetrieveUpdateDestroyAPIView):
	serializer_class = UserProfileSerializer
	permission_classes = (IsOwnerOrAdmin,)
	queryset = UserProfile.objects.all()

# avatar upload
class AvatarUploadView(APIView):
	parser_classes = (MultiPartParser,)
	permission_classes = (permissions.AllowAny,)

	def put(self, request, format=None):
		file_obj = request.data['file']

		avatarupload = AvatarUpload.objects.get(user=request.user)

		avatarupload.file = file_obj
		avatarupload.save()

		return Response({'url':'{}/{}'.format(settings.MEDIA_ROOT,avatarupload.file)},status=status.HTTP_200_OK)


