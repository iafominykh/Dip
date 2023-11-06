from django.conf import settings
from django.db import models
from users.models import NULLABLE


# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    preview = models.ImageField(**NULLABLE, upload_to='courses/', verbose_name='Превью')
    description = models.TextField(**NULLABLE, verbose_name='Описание')
    url = models.URLField(**NULLABLE, verbose_name='Ссылка')
    is_public = models.BooleanField(default=False)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE,
                              verbose_name='Создатель')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Lesson(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, **NULLABLE, verbose_name='Курс')
    title = models.CharField(max_length=150, verbose_name='Название')
    description = models.TextField(**NULLABLE, verbose_name='Описание')
    preview = models.ImageField(**NULLABLE, upload_to='courses/', verbose_name='Превью')
    lesson_url = models.URLField(**NULLABLE, verbose_name='Ссылка на урок')
    is_public = models.BooleanField(default=False)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE,
                              verbose_name='Создатель')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'


