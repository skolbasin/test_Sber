# Generated by Django 5.0.3 on 2024-04-15 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='books_taken',
            field=models.ManyToManyField(blank=True, null=True, related_name='readers', to='app.book', verbose_name='Взятые книги'),
        ),
    ]
