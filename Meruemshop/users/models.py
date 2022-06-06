
from django.db import models
from django.templatetags.static import static
from django.conf import settings
from django.contrib.auth.models import AbstractUser, BaseUserManager


class AuthUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an e-mail address.')

        user = self.model(
            email=self.normalize_email(email)
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class AuthUser(AbstractUser):
    username = None
    email = models.EmailField(verbose_name='email', max_length=255, unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = AuthUserManager()

    def __str__(self):
        return self.email

    def __repr__(self):
        return self.__str__()


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(upload_to='profile_images/', null=True, default=None)

    @property
    def image(self):
        if self.avatar:
            return self.avatar.url

        return static('images/defaultUser.jpg')
