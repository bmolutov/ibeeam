from custom_auth.models import User


def delete_user(profile_id):
    user = User.objects.filter(profile_id=profile_id).first()
    if not user:
        return False
    user.delete()
    return True
