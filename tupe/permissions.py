from rest_framework import permissions


# класс который позволяет просматривать клиент, а редачить только админ
class IsAdminReadOnly(permissions.BasePermission):
    # делаем ограничение доступа
    def has_permission(self, request, view):
        # если медот безопасный то даем для всех доступ SAFE_METHODS(на чтение данных)
        if request.method in permissions.SAFE_METHODS:
            return True

        # если вошел админ (иначе только для админа)
        return bool(request.user and request.user.is_staff)




#  класс который может менять запись автор, а просматривать толлько пользователи
class IsOwnerOrReadOnly(permissions.BasePermission):
    # метод который разрешает на ур одной записи
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user == request.user
