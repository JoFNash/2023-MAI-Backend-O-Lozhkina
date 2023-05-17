import datetime

from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class Profile(models.Model):
    email = models.TextField(verbose_name='Почта')
    password = models.TextField(verbose_name='Пароль')
    registration_date = models.DateTimeField(default=datetime.datetime.utcnow, verbose_name='Дата регистрации')

    class Meta:
        db_table = 'profiles'

    def __str__(self):
        return self.email


class Movie(models.Model):
    name = models.TextField(verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    price = models.IntegerField(validators=[MinValueValidator(0)], verbose_name='Цена')

    class Meta:
        db_table = 'movies'

    def __str__(self):
        return self.name


class Purchase(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=False, verbose_name='Пользователь')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, blank=False, verbose_name='Фильм')
    purchase_date = models.DateTimeField(default=datetime.datetime.utcnow, verbose_name='Дата покупки')
    rating = models.IntegerField(null=True, validators=[MinValueValidator(0), MaxValueValidator(10)], verbose_name="Рейтинг")

    class Meta:
        db_table = 'purchases'
