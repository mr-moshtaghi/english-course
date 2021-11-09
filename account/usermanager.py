from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):

    def _create_user(self, cellphone, password, **extra_fields):
        """
        Create and save a user with the given username, email, and password.
        """
        self.cellphone = cellphone
        user = self.model(cellphone=cellphone, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, cellphone, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(cellphone, password, **extra_fields)

    def create_superuser(self, cellphone, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(cellphone, password, **extra_fields)
