import datetime

from django.db import models  # noqa F401


class Pokemon(models.Model):
    id = models.AutoField(auto_created=True, primary_key=True)
    title = models.CharField(max_length=200)
    title_en = models.CharField(max_length=200, blank=True)
    title_jp = models.CharField(max_length=200, blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True)
    description = models.TextField(blank=True)
    previous_evolution = models.ForeignKey(
        "self",
        related_name='next_evolutions',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )

    def __str__(self):
        return f'{self.title}'


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    lat = models.FloatField(verbose_name="Широта")
    lon = models.FloatField(verbose_name="Долгота")
    appeared_at = models.DateTimeField(default=datetime.datetime.now())
    disappeared_at = models.DateTimeField(default=datetime.datetime.now())
    level = models.IntegerField(default=1)
    hp = models.IntegerField(default=100)
    attack = models.IntegerField(default=5)
    protection = models.IntegerField(default=3)
    endurance = models.IntegerField(default=2)

    def __str__(self):
        return f' Покемон: {self.pokemon.title} Широта: {self.lat} Долгота: {self.lon}'
