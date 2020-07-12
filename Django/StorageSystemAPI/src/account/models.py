from django.conf import settings
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from phonenumber_field.modelfields import PhoneNumberField
from rest_framework.authtoken.models import Token


class MyAccountManager(BaseUserManager):
    def create_user(self, email, name, surname, cell_phone, address, residence, password=None):
        if not email:
            raise ValueError("User must have an email address.")
        if not name:
            raise ValueError("User must have a name.")
        if not surname:
            raise ValueError("User must have a surname.")
        if not cell_phone:
            raise ValueError("User must have a cell phone.")
        if not address:
            raise ValueError("User must have an adress.")
        if not residence:
            raise ValueError("User must have a residence.")

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            surname=surname,
            cell_phone=cell_phone,
            address=address,
            residence=residence,
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, surname, cell_phone, address, residence, password):
        user = self.create_user(
            email=self.normalize_email(email),
            name=name,
            password=password,
            surname=surname,
            cell_phone=cell_phone,
            address=address,
            residence=residence,
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    data_joined = models.DateTimeField(verbose_name="data joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    phone = PhoneNumberField(blank=True, help_text="Contact phone number. Add '+385' in front for Croatia.")
    cell_phone = PhoneNumberField(blank=True, help_text="Contact cell phone number. Add '+385' in front for Croatia.", unique=True)
    address = models.CharField(max_length=50)
    residence = models.CharField(max_length=50)

    # Field used to login
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name', 'surname', 'cell_phone', 'address', 'residence',]

    objects = MyAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True


class Location(models.Model):
    latitude = models.DecimalField(max_digits=8, decimal_places=5)
    longitude = models.DecimalField(max_digits=8, decimal_places=5)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    time = models.DateTimeField(verbose_name="time", auto_now=True)

    def __str__(self):
        return str(self.latitude) + ", " + str(self.longitude)

    class Meta:
        ordering = ['latitude', 'longitude']


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)