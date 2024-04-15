from django.db import models
from django.db.models import PositiveIntegerField
from django.utils.translation import gettext_lazy as _

from .config import validate_username, validate_age


class Library(models.Model):
    """
    Модель библиотеки
    """

    class Meta:
        verbose_name = _("Библиотека")
        verbose_name_plural = _("Библиотеки")

    name = models.CharField(max_length=100, null=False, verbose_name=_("Название организации"))
    address = models.CharField(max_length=200, verbose_name=_("Адрес"))
    state_facility = models.BooleanField(verbose_name=_("Государственный"))

    def __str__(self):
        return self.name


class UserAccount(models.Model):
    """
    Модель пользователя
    """
    class Meta:
        verbose_name = _("Пользователь")
        verbose_name_plural = _("Пользователи")

    username = models.CharField(max_length=50, validators=[validate_username], verbose_name=_("Фамилия Имя"))
    age = PositiveIntegerField(default=0, validators=[validate_age], verbose_name=_("Возраст"))
    email = models.EmailField(verbose_name=_("Почта"))
    image = models.ImageField(
        null=True,
        blank=True,
        verbose_name=_("Фото"),
    )
    books_taken = models.ManyToManyField('Book',
                                         null=True,
                                         blank=True,
                                         related_name='readers',
                                         verbose_name=_("Взятые книги"))

    def __str__(self):
        return self.username


class Book(models.Model):
    """
    Модель книги
    """
    class Meta:
        verbose_name = _("Книга")
        verbose_name_plural = _("Книги")

    title = models.CharField(max_length=100, verbose_name=_("Название книги"))
    author = models.CharField(max_length=100, verbose_name=_("Автор/Авторы"))
    publishing_house = models.CharField(max_length=100, verbose_name=_("Издательство"))
    library = models.ForeignKey(Library, on_delete=models.CASCADE, verbose_name=_("Библиотека"))
    users = models.ManyToManyField(UserAccount,
                                   null=True,
                                   blank=True,
                                   related_name='books_read',
                                   verbose_name=_("Читатели"))
    remain_count = PositiveIntegerField(default=0, verbose_name=_("Остатки на складе"))

    def __str__(self):
        return self.title
