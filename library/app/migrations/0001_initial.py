# Generated by Django 5.0.3 on 2024-04-15 10:47

import app.config
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название организации')),
                ('address', models.CharField(max_length=200, verbose_name='Адрес')),
                ('state_facility', models.BooleanField(verbose_name='Государственный')),
            ],
            options={
                'verbose_name': 'Библиотека',
                'verbose_name_plural': 'Библиотеки',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название книги')),
                ('author', models.CharField(max_length=100, verbose_name='Автор/Авторы')),
                ('publishing_house', models.CharField(max_length=100, verbose_name='Издательство')),
                ('remain_count', models.PositiveIntegerField(default=0, verbose_name='Остатки на складе')),
                ('library', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.library', verbose_name='Библиотека')),
            ],
            options={
                'verbose_name': 'Книга',
                'verbose_name_plural': 'Книги',
            },
        ),
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, validators=[app.config.validate_username], verbose_name='Фамилия Имя')),
                ('email', models.EmailField(max_length=254, verbose_name='Почта')),
                ('image', models.ImageField(blank=True, null=True, upload_to='', verbose_name='Фото')),
                ('books_taken', models.ManyToManyField(related_name='readers', to='app.book', verbose_name='Взятые книги')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
        migrations.AddField(
            model_name='book',
            name='users',
            field=models.ManyToManyField(blank=True, null=True, related_name='books_read', to='app.useraccount', verbose_name='Читатели'),
        ),
    ]
