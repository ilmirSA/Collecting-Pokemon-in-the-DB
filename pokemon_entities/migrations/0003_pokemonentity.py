# Generated by Django 3.1.14 on 2025-02-05 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon_entities', '0002_pokemon_avatar'),
    ]

    operations = [
        migrations.CreateModel(
            name='PokemonEntity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.FloatField(verbose_name='Широта')),
                ('lon', models.FloatField(verbose_name='Долгота')),
            ],
        ),
    ]
