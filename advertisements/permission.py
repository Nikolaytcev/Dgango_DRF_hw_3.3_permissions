from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.user.id in [obj.creator.id, 1]  # 1 is admin
