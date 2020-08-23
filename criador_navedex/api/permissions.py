from rest_framework import permissions

class IsResponsibleForNaverOrReadOnly(permissions.BasePermission):
    """
    Permissão para DELETE e UPDATE somente de navers vinculados a si,
    caso contrário, somente pode fazer requisições 'read only'
    GET, HEAD, OPTIONS (safe methods)
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.user == request.user

class IsResponsibleForProjectOrReadOnly(permissions.BasePermission):
    """
    Permissão para DELETE e UPDATE somente de projetos vinculados a si,
    caso contrário, somente pode fazer requisições 'read only'
    GET, HEAD, OPTIONS (safe methods)
    """

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.naver_id == request.user.id
