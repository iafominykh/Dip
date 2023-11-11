
from django.db import models
from users.models import NULLABLE, User



class Course(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    preview = models.ImageField(**NULLABLE, upload_to='courses/', verbose_name='Превью')
    description = models.TextField(**NULLABLE, verbose_name='Описание')
    url = models.URLField(**NULLABLE, verbose_name='Ссылка')
    is_public = models.BooleanField(default=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, **NULLABLE,
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
    owner = models.ForeignKey(User, on_delete=models.CASCADE, **NULLABLE,
                              verbose_name='Создатель')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'


class Test(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='Урок')
    test_title = models.CharField(max_length=150, verbose_name='Название')
    description = models.TextField(**NULLABLE, verbose_name='Описание')
    is_public = models.BooleanField(default=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, **NULLABLE,
                              verbose_name='Создатель')

    def __str__(self):
        return f'{self.test_title}'

    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'


class Question(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE, verbose_name='Тест')
    question_text = models.CharField(max_length=200, verbose_name='Текст вопроса')

    def __str__(self):
        return f'{self.question_text}'

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, verbose_name='Вопрос')
    answer_text = models.CharField(max_length=200, verbose_name='Текст ответа')
    is_correct = models.BooleanField(default=False, verbose_name='Правильный ответ')

    def __str__(self):
        return f'{self.answer_text}'

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'
