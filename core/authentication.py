import jwt
from delivery_club.settings import SECRET
from rest_framework.authentication import BaseAuthentication

from .models import User


class Authentication(BaseAuthentication):

    def authenticate(self, request):
        if 'HTTP_AUTHORIZATION' in request.META:
            token = request.META.get('HTTP_AUTHORIZATION')
            token = token.split()[1]
            try:
                payload = jwt.decode(token.encode('utf-8'), SECRET)
                if 'user_id' not in payload:
                    raise Exception
                user_id = payload['user_id']
                user = User.objects.get(id=user_id)
                return user, True
            except Exception:
                return
