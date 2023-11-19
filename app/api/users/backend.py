from django.contrib.auth.backends import ModelBackend

from .models import Account


class Authentication(ModelBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        if email is None or password is None:
            email = request.POST.get('username')
            password = request.POST.get('password')

        try:
            user = Account.objects.get(email=email)
        except Account.DoesNotExist:
            return None
        else:
            check = user.check_password(password)
            if check and self.user_can_authenticate(user):
                return user
