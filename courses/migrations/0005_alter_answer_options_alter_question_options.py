# Generated by Django 4.2.7 on 2023-11-11 07:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_test_question_answer'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='answer',
            options={'verbose_name': 'Ответ', 'verbose_name_plural': 'Ответы'},
        ),
        migrations.AlterModelOptions(
            name='question',
            options={'verbose_name': 'Вопрос', 'verbose_name_plural': 'Вопросы'},
        ),
    ]
