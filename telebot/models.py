from django.db import models

# Create your models here.

class TeleSettings(models.Model):
    tg_token = models.CharField(verbose_name='Токен', max_length=200)
    tg_chat = models.CharField(verbose_name='Чат id', max_length=200)
    tg_message = models.TextField(verbose_name='Текст сообщения')

    def __str__(self):
        return self.tg_chat

    class Meta:
        verbose_name = 'настройку'
        verbose_name_plural = 'настройки'