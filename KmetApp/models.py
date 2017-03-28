from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser,
                                        PermissionsMixin)


class CustomUserManager(BaseUserManager):
    """ Custom Manager """
    def create_user(self, email, password=None):
        """ create user method"""
        if not email:
            raise ValueError("User more imet email!")

        email = email.lower()
        user = self.model(email=CustomUserManager.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        user.is_staff = False
        user.is_admin = False
        user.is_active = True
        return user

    def create_superuser(self, email, password):
        """Create Super User"""
        user = self.create_user(
            email,
            password=password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    """User Model"""
    email = models.EmailField(max_length=255, unique=True, db_index=True)

    USERNAME_FIELD = 'email'
    name = models.CharField(max_length=100)
    last_Name = models.CharField(max_length=100)
    adress = models.CharField(max_length=50)
    zip_Code = models.IntegerField()
    city = models.CharField(max_length=50)
    phone_Number = models.CharField(max_length=20)

    objects = CustomUserManager()

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        self.email = self.email.lower()
        super(User, self).save(*args, **kwargs)


class Selling(models.Model):
    """Model For Sellings"""
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    quantity = models.IntegerField()
    description = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    seller = models.ForeignKey(User)
    is_Active = models.BooleanField(default=True)
    picture = models.ImageField(upload_to='KmetApp/Media/', null=True, blank=True)
    origin = models.CharField(max_length=50)


class Order_Selling(models.Model):
    """Orders for Sellings"""
    price_Order = models.DecimalField(max_length=10, max_digits=5,
                                      decimal_places=2)
    quantity_Order = models.IntegerField()
    is_Completed = models.BooleanField(default=False)
    date_Submission = models.DateTimeField(auto_now_add=True, blank=True)
    date_Completed = models.DateTimeField(null=True, blank=True)
    selling = models.ForeignKey(Selling)
    buyer = models.ForeignKey(User)


class Basket(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_length=10, max_digits=5, decimal_places=2)
    quantity = models.IntegerField()
    total_Amount = models.IntegerField()
    description = models.CharField(max_length=200)
    seller = models.ForeignKey(User)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    is_Active = models.BooleanField(default=True)
    picture = models.ImageField(upload_to='KmetApp/Media/', null=True, blank=True)
    origin = models.CharField(max_length=50)


class Order_Basket(models.Model):
    price_Order = models.DecimalField(max_length=10, max_digits=5, decimal_places=2)
    quantity_Order = models.IntegerField()
    date_Submission = models.DateTimeField(auto_now_add=True, blank=True)
    date_Completed = models.DateTimeField(default=None, blank=True)
    frequency = models.CharField(max_length=40)
    is_Completed = models.BooleanField(default=False)
    basket = models.ForeignKey(Basket)
    buyer = models.ForeignKey(User)

"""
class News(models.Model):
    title = models.CharField(max_length = 100, blank=True)
    description = models.CharField(max_length = 50000, blank=True)
    post_date = models.DateTimeField(default= None, blank= True)

class Attachments(models.Model):
    picture = models.ImageField(upload_to='img/News/' , default='img/Basket/default.jpg')
    news = models.ForeignKey(News)
"""

