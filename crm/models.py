from django.db import models

# Create your models here.
class StatusCrm(models.Model):
    status_name = models.CharField(max_length=200, verbose_name='Название статуса')

    def __str__(self):
        return self.status_name

    class Meta:
        verbose_name = 'статус'
        verbose_name_plural = 'статусы'


class Order(models.Model):
    order_dt = models.DateTimeField(verbose_name='Дата и время', auto_now=True)
    order_name = models.CharField(verbose_name='Имя', max_length=200)
    order_phone = models.CharField(verbose_name='Телефон', max_length=200)
    order_status =models.ForeignKey(StatusCrm, on_delete=models.PROTECT, null=True, blank=True, verbose_name='Статус')

    def __str__(self):
        return self.order_name

    class Meta:
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'


class CommentCrm(models.Model):
    comment_binding = models.ForeignKey(Order, on_delete=models.CASCADE, verbose_name='Заявка')
    comment_text = models.TextField(verbose_name='Текст комментария')
    comment_dt = models.DateTimeField(verbose_name='Дата создания', auto_now=True,)

    def __str__(self):
        return self.comment_text

    class Meta:
        verbose_name = 'комментарий'
        verbose_name_plural = 'комментарии'