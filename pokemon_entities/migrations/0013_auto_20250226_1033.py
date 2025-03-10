# Generated by Django 3.1.14 on 2025-02-26 07:33

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0012_auto_20250226_0959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemonentity',
            name='appeared_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2025, 2, 26, 7, 33, 6, 740156, tzinfo=utc), null=True, verbose_name='Время появления'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='attack',
            field=models.PositiveIntegerField(blank=True, default=5, null=True, verbose_name='Атака'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='disappeared_at',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2025, 2, 26, 7, 33, 6, 740156, tzinfo=utc), null=True, verbose_name='Время исчезновения'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='endurance',
            field=models.PositiveIntegerField(blank=True, default=2, null=True, verbose_name='Выносливость'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='hp',
            field=models.PositiveIntegerField(blank=True, default=100, null=True, verbose_name='Здоровье'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='level',
            field=models.PositiveIntegerField(blank=True, default=1, null=True, verbose_name='Уровень'),
        ),
        migrations.AlterField(
            model_name='pokemonentity',
            name='protection',
            field=models.PositiveIntegerField(blank=True, default=3, null=True, verbose_name='Защита'),
        ),
    ]
