from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser


class TimeStampedModel(models.Model):

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class User(AbstractUser, TimeStampedModel):
    pass


class LoginHistory(TimeStampedModel):
    user = models.ForeignKey(User, verbose_name=_("user"), on_delete=models.CASCADE)
    successful = models.BooleanField(_("successful"))

    def __str__(self):
        return f"{self.user} - {self.os} {self.device}"

    class Meta:
        verbose_name = _("Login history")
        verbose_name_plural = _("Login histories")
