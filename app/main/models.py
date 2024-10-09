from django.db import models


class Services(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    image = models.ImageField(upload_to='services_images', blank=True, null=True, verbose_name='Изображение')
    price = models.DecimalField(max_digits=7, decimal_places=2, verbose_name='Цена')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    
    class Meta:
        db_table = 'Услуги'
        verbose_name = 'Услугу'
        verbose_name_plural = 'Услуги'
        
    def __str__(self):
        return self.name
        