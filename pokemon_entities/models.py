import datetime

from django.db import models  # noqa F401


class Pokemon(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    title = models.CharField(verbose_name="Имя покемона",max_length=200)
    title_en = models.CharField(verbose_name="Имя покемона на английском", max_length=200, blank=True)
    title_jp = models.CharField(verbose_name="Имя покемона на японском", max_length=200, blank=True)
    avatar = models.ImageField(verbose_name="Картинка", upload_to='avatars/', blank=True)
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
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    lat = models.FloatField(verbose_name="Широта")
    lon = models.FloatField(verbose_name="Долгота")
    appeared_at = models.DateTimeField(verbose_name="Время появления",default=datetime.datetime.now(),null=True, blank=True)
    disappeared_at = models.DateTimeField(verbose_name="Время исчезновения", default=datetime.datetime.now(),null=True, blank=True)
    level = models.IntegerField(verbose_name="Уровень", default=1,null=True, blank=True)
    hp = models.IntegerField(verbose_name="Здоровье",default=100,null=True, blank=True)
    attack = models.IntegerField(verbose_name="Атака",default=5,null=True, blank=True)
    protection = models.IntegerField(verbose_name="Защита",default=3,null=True, blank=True)
    endurance = models.IntegerField(verbose_name="Выносливость",default=2,null=True, blank=True)
    def __str__(self):
        return f' Покемон: {self.pokemon.title} Широта: {self.lat} Долгота: {self.lon}'
