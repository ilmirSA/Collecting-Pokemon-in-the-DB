import datetime

from django.db import models  # noqa F401
from django.utils import timezone

class Pokemon(models.Model):
    title = models.CharField(verbose_name="Имя покемона",max_length=200)
    title_en = models.CharField(verbose_name="Имя покемона на английском", max_length=200, blank=True)
    title_jp = models.CharField(verbose_name="Имя покемона на японском", max_length=200, blank=True)
    avatar = models.ImageField(verbose_name="Картинка", upload_to='avatars/', blank=True, null=True)
    description = models.TextField(verbose_name="Описание",blank=True)
    previous_evolution = models.ForeignKey(
        "self",
        related_name='next_evolutions',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        verbose_name="Предыдущая эволюция"
    )

    def __str__(self):
        return f'{self.title}'


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, verbose_name="Покемон", related_name='entities',)
    lat = models.FloatField(verbose_name="Широта")
    lon = models.FloatField(verbose_name="Долгота")
    appeared_at = models.DateTimeField(verbose_name="Время появления", default=timezone.now, null=True, blank=True)
    disappeared_at = models.DateTimeField(verbose_name="Время исчезновения", default=timezone.now, null=True, blank=True)
    level = models.PositiveIntegerField(verbose_name="Уровень", default=1,null=True, blank=True)
    hp = models.PositiveIntegerField(verbose_name="Здоровье", default=100,null=True, blank=True)
    attack = models.PositiveIntegerField(verbose_name="Атака", default=5,null=True, blank=True)
    protection = models.PositiveIntegerField(verbose_name="Защита", default=3,null=True, blank=True)
    endurance = models.PositiveIntegerField(verbose_name="Выносливость", default=2,null=True, blank=True)
    def __str__(self):
        return f' Покемон: {self.pokemon.title} Широта: {self.lat} Долгота: {self.lon}'
