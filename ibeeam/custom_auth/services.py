from django.contrib.auth.models import User


def delete_user(username):
    user = User.objects.filter(username=username).first()
    if not user:
        return False
    user.delete()
    return True
