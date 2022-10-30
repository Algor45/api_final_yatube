from rest_framework.permissions import SAFE_METHODS, BasePermission


class AuthorPermissionOrReadOnly(BasePermission):
    """Разрешение на изменение постов только для автора или чтение."""

    message = 'У вас нет прав на эту операцию.'

    def has_permission(self, request, view):
        """Проверка метод запроса безопасен или пользователь авторизован."""
        return (
            request.method in SAFE_METHODS
            or request.user.is_authenticated
        )

    def has_object_permission(self, request, view, obj):
        """Сравнение автора объекта с текущим пользователем."""

        return obj.author == request.user


class ReadOnly(BasePermission):
    """Разрешение только для чтения."""
    def has_permission(self, request, view):
        """Проверка или метод запроса безопасен."""
        return request.method in SAFE_METHODS
