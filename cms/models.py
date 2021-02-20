from django.db import models

# Create your models here.
class CmsSlider(models.Model):
    cms_img = models.ImageField(upload_to='sliderimg/')
    cms_title = models.CharField(verbose_name='Заголовок', max_length=200)
    cms_text = models.TextField(verbose_name='Текст', max_length=200)
    cms_css = models.CharField(verbose_name='CSS класс', max_length=200, default='-', null=True)


    def __str__(self):
        return self.cms_title

    class Meta:
        verbose_name = 'слайд'
        verbose_name_plural = 'слайды'