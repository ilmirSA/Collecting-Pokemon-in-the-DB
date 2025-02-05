import folium
from django.http import HttpResponseNotFound
from django.shortcuts import render
from django.utils.timezone import localtime

from pogomap import settings
from pokemon_entities.models import PokemonEntity

MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = (
    'https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision'
    '/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832'
    '&fill=transparent'
)


def add_pokemon(folium_map, lat, lon, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        # Warning! `tooltip` attribute is disabled intentionally
        # to fix strange folium cyrillic encoding bug
        icon=icon,
    ).add_to(folium_map)


def show_all_pokemons(request):
    pokemons_all = PokemonEntity.objects.filter(appeared_at__lte=localtime(), disappeared_at__gte=localtime(), )

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon in pokemons_all:
        image_url = request.build_absolute_uri(f"{settings.MEDIA_URL}{pokemon.pokemon.avatar}")
        add_pokemon(
            folium_map, pokemon.lat,
            pokemon.lon,
            image_url
        )

    pokemons_on_page = []
    for pokemon in pokemons_all:
        image_url = request.build_absolute_uri(f"{settings.MEDIA_URL}{pokemon.pokemon.avatar}")
        pokemons_on_page.append({
            'pokemon_id': pokemon.pokemon.id,
            'img_url': image_url,
            'title_ru': pokemon.pokemon.title
        })

    return render(request, 'mainpage.html', context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):
    pokemon_all = []
    pokemons = PokemonEntity.objects.filter(pokemon__id=pokemon_id)

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)

    for pokemon in pokemons:
        if pokemon.pokemon.id == int(pokemon_id):

            image_url = request.build_absolute_uri(f"{settings.MEDIA_URL}{pokemon.pokemon.avatar}")

            pokemon_all.append({
                "pokemon_id": pokemon.pokemon.id,
                "title_ru": pokemon.pokemon.title,
                "img_url": image_url
            })

            add_pokemon(
                folium_map, pokemon.lat,
                pokemon.lon,
                image_url
            )

            break
        else:
            return HttpResponseNotFound('<h1>Такой покемон не найден</h1>')

    return render(request, 'pokemon.html', context={
        'map': folium_map._repr_html_(), 'pokemon': pokemon_all
    })
