from django.contrib.auth.models import User
from django.contrib.auth import login
from django.db import IntegrityError

from posts.utils import generate_username

# Checks whether the user is authenticated. If not,
# it creates/generates the user and logs it in.
def ensure_user(get_response):
    def middleware(request):
        if not request.user.is_authenticated:
            # Attempt to create user 10 times. Only retries
            # if the username is already taken.
            user = None
            for _ in range(0, 10):
                try:
                    user = User.objects.create_user(generate_username())
                    user.save()
                except IntegrityError:
                    continue
                else:
                    break
            
            login(request, user)
            
        return get_response(request)

    return middleware