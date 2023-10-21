from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.users.models import TimeStampedModel, User


class Post(TimeStampedModel):
    title = models.CharField(max_length=200)
    body = models.TextField()
    liked = models.ManyToManyField(User, blank=True, related_name='liked_post')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_post')

    def __str__(self):
        return str(self.title)


class RequestHistory(TimeStampedModel):
    user = models.ForeignKey(User, verbose_name=_("user"), on_delete=models.CASCADE)
    ip = models.CharField(_("ip"), max_length=50)
    browser = models.CharField(_("browser"), max_length=50, blank=True)

    def __str__(self):
        return f"{self.user} - {self.os} {self.device}"

    class Meta:
        verbose_name = _("Request history")
        verbose_name_plural = _("Request histories")
