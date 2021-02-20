from django.db import models

# Create your models here.

class PriceCard(models.Model):
    pc_value = models.CharField(verbose_name='Цена', max_length=20)
    pc_description = models.CharField(max_length=200, verbose_name='Описание')

    def __str__(self):
        return self.pc_value

    class Meta:
        verbose_name = 'цены'
        verbose_name_plural = 'цены'


class PriceTable(models.Model):
    pt_title = models.CharField(verbose_name='Услуга', max_length=200)
    pt_old_price = models.CharField(verbose_name='Старая цена', max_length=200)
    pt_new_price = models.CharField(verbose_name='Новая цена', max_length=200)

    def __str__(self):
        return self.pt_title

    class Meta:
        verbose_name = 'услуги'
        verbose_name_plural = 'услуги'

