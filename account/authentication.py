from .models import User

class EmailAuthBackend:
  def authenticate(self, request, username = None, password = None):
    try:
      user = User.objects.get(email = username)
      if user.check_password(password):
        return user
      return None
    except:
      return None

  def get_user(self, user_id):
    try:
      return User.objects.get(pk = user_id)
    except:
      return None