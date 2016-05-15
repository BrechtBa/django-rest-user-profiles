from rest_framework import permissions
from rest_framework_jwt.utils import jwt_decode_handler

			
class IsOwnerOrAdmin(permissions.BasePermission):
	"""
	Custom permission to only allow owners of an object and the admin to view and edit it.
	"""
	
	def has_object_permission(self, request, view, obj):
		
		if hasattr(obj,'user'):
			return (obj.user == request.user) or request.user.is_staff
		else:
			return (obj == request.user) or request.user.is_staff
	
class IsAdminOrReadOnly(permissions.BasePermission):
	"""
	Custom permission to only allow owners of an object to edit it.
	"""

	def has_object_permission(self, request, view, obj):
		# Read permissions are allowed to any request,
		# so we'll always allow GET, HEAD or OPTIONS requests.
		if request.method in permissions.SAFE_METHODS:
			return True

		# Write permissions are only allowed to the admin
		return request.user.is_staff
