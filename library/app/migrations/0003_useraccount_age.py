# Generated by Django 5.0.3 on 2024-04-15 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_useraccount_books_taken'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='age',
            field=models.PositiveIntegerField(default=0, verbose_name='Возраст'),
        ),
    ]