# Generated by Django 3.1.7 on 2021-04-19 15:22

import app.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(upload_to=app.models.avatar_upload_to, verbose_name='Аватар')),
                ('count', models.IntegerField(default=0, verbose_name='Количество вопросов и ответов у пользователя')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Имя')),
                ('count', models.IntegerField(default=0, verbose_name='Количество вопросов по тегу')),
            ],
            options={
                'verbose_name': 'Тег',
                'verbose_name_plural': 'Теги',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128, verbose_name='Заголовок')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('text', models.TextField(verbose_name='Текст')),
                ('rating', models.IntegerField(default=0, verbose_name='Рейтинг')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.profile', verbose_name='Автор')),
                ('tags', models.ManyToManyField(blank=True, to='app.Tag', verbose_name='Теги')),
            ],
            options={
                'verbose_name': 'Вопрос',
                'verbose_name_plural': 'Вопросы',
            },
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('text', models.TextField(verbose_name='Текст')),
                ('is_correct', models.BooleanField(default=False, verbose_name='Корректность ответа')),
                ('rating', models.IntegerField(default=0, verbose_name='Рейтинг')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.profile', verbose_name='Автор')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.question', verbose_name='Вопрос')),
            ],
            options={
                'verbose_name': 'Ответ',
                'verbose_name_plural': 'Ответы',
            },
        ),
    ]
