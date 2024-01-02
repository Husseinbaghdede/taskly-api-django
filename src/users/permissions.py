from rest_framework import permissions

class isUserOwnerOrGetAndPostOnly(permissions.BasePermission):
    """
    Custom permission for Userviewset 
    to only allow the user to edit their
    own user otherwise they can only do get and post
    """
    
    def has_permission(self,request,view):
        return True
    
    def has_object_permission(self,request,view,obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        if not request.user.is_anonymous:
            return request.user == obj
        return False
class isProfileOwnerOrReadOnly(permissions.BasePermission):
    """
      Custom permissions for profileviewset to only allow user to edit their own profile. otherwise get and post only.
    """
    def has_permission(self,request,view):
        return True
    def has_object_permission(self,request,view,obj):    
        if request.method in permissions.SAFE_METHODS:
            return True
        if not request.user.is_anonymous:
            return request.user.profile == obj
        return False

        