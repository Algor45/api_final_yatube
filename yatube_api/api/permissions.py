from rest_framework.permissions import SAFE_METHODS, BasePermission


class AuthorPermissionOrReadOnly(BasePermission):
    """Разрешение на изменение постов только для автора или чтение."""

    message = 'У вас нет прав на эту операцию.'

    def has_object_permission(self, request, view, obj):
        """Сравнение автора объекта с текущим пользователем
           а также проверка на безопасные методы."""

        return request.method in SAFE_METHODS or obj.author == request.user
