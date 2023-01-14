from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Account(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Conta"
        verbose_name_plural = "Contas"

    def __str__(self):
        return self.user.email

    def delete(self, using=None, keep_parents=False):
        self.user.delete()
