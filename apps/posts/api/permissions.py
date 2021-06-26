from rest_framework import permissions
from rest_framework import permissions

# https://www.django-rest-framework.org/api-guide/permissions/#examples
class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        print(obj.author)
        print(request.user)
        return obj.author == request.user