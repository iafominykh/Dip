from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """ Класс владельца контента """
    message = "У вас нет прав создателя!"

    def has_object_permission(self, request, view, object):
        if request.user == object.owner:
            return True
        return False