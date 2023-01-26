from django.db import models
from django.contrib.auth.models import User

class Tupe(models.Model):
    # class Meta:
    #     verbose_name = 'Вышивка одежды'
    #     verbose_name_plural = 'Вышивка одежды'
    #     ordering = ['time_create', 'title']
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    content = models.TextField(blank=True, verbose_name='Текст')
    time_create = models.DateTimeField(auto_now_add=True,null=True, blank=True)
    time_update = models.DateTimeField(auto_now=True, verbose_name='Текст', null=True, blank=True)
    is_published = models.BooleanField(default=True, null=True, blank=True)
    cat = models.ForeignKey('Category', verbose_name='Категория', on_delete=models.PROTECT, null=True,)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)

    # on_delete=models.CASCADE - удаляет все поля если удалил пользователь

    def __str__(self):
        return self.title


class Category(models.Model):
    # class Meta:
    #     verbose_name = 'Категории'
    #     verbose_name_plural = 'Категории'
    #     ordering = ['id']
    name = models.CharField(max_length=100, db_index=True, verbose_name='Категория')

    def __str__(self):
        return self.name