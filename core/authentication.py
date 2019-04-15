import jwt
from delivery_club.settings import SECRET
from rest_framework.authentication import BaseAuthentication

from .models import User


class Authentication(BaseAuthentication):

    def authenticate(self, request):
        if 'authorization' in request.META:
            token = request.META.get('Authorization')
            token = token.split()[1]
            try:
                payload = jwt.decode(token, SECRET, leeway=0)
                if 'user_id' not in payload:
                    raise Exception
                user_id = payload['user_id']
                user = User.objects.get(id=user_id)
                return user, True
            except Exception:
                return
