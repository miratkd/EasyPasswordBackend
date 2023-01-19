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

class Password(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE, verbose_name='conta')
    site = models.CharField(max_length=50, help_text='Limite de 50 characteres.')
    password = models.CharField(max_length=50, help_text='Limite de 50 characteres.', verbose_name='senha')

    class Meta:
        verbose_name_plural = "Senhas"
        verbose_name = "Senha"

    def __str__(self):
        return self.site + '-' + self.password
