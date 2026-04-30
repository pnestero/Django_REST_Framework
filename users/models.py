from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from lesson_course.models import Course, Lesson


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=35, blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    avatar = models.ImageField(upload_to='users/avatars/', blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


class Payment(models.Model):
    class PaymentMethod(models.TextChoices):
        CASH = 'cash', 'Наличные'
        TRANSFER = 'transfer', 'Перевод на счет'

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='payments')
    payment_date = models.DateTimeField(auto_now_add=True)
    paid_course = models.ForeignKey(Course, on_delete=models.CASCADE, null=True, blank=True, related_name='payments')
    paid_lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, null=True, blank=True, related_name='payments')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=10, choices=PaymentMethod.choices)

    def __str__(self):
        return f"{self.user.email} - {self.amount} - {self.payment_method}"
