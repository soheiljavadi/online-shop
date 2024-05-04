from rest_framework import permissions

class IsAdminOrSeller(permissions.BasePermission):
    def has_permission(self, request, view):
        # Check if the user is authenticated
        if not request.user.is_authenticated:
            return False

        # Check if the user is an admin or a seller
        user = request.user
        is_admin = user.is_staff  # Assumes that all admins are marked as staff in Django admin
        is_seller = hasattr(user, 'userprofile') and user.Costomuser.is_seller
        
        return is_admin or is_seller