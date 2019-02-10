from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter
import folium
import progressbar


def mapa_build():
    """
    Builds html file with map with two layers(population and films by year)
    """
    year = input()
    mapa = folium.Map(tiles="Mapbox Bright", zoom_start=1000)
    mapa.add_child(population_layer())
    mapa.add_child(film_by_year_layer(collect_data("locations.list", year), year))
    mapa.add_child(folium.LayerControl())
    mapa.save('Map_'+year+'.html')


def population_layer():
    """
    (None) -> FeatureGroup
    Builds population layer
    """
    fg = folium.FeatureGroup(name="Population")
    fg.add_child(folium.GeoJson(data=open('world.json', 'r',
                                encoding='utf-8-sig').read(),
                                style_function=lambda x: {'fillColor':'green'
                                if x['properties']['POP2005'] < 10000000
                                else 'orange'
                                if 10000000 <= x['properties']['POP2005'] < 20000000
                                else 'red'}))
    return fg


def film_by_year_layer(data, year):
    """
    (list, str) -> FeatureGroup
    Builds layer with films on locations by user's year
    """
    fg = folium.FeatureGroup(name="Filmed in " + year)
    bar = progressbar.ProgressBar(max_value=len(data))
    i = 0
    for each in data:
        try:
            fg.add_child((folium.Marker(location=generate_coordinates(each[1]),
                                        popup=each[0],
                                        icon=folium.Icon())))
            bar.update(i)
            i += 1
        except:
            bar.update(i)
            i += 1
            continue
    return fg


def collect_data(file_name, year):
    """
    (str, str) -> list
    Gets .list file and year, returns list with tuples (film name, location)
    """
    with open(file_name, 'r', encoding="Latin-1") as file:
        film_data = []
        bar = progressbar.ProgressBar(max_value=1241786)
        i = 0
        for line in file.readlines():
            if "\t" in line and line.split("(")[1][:4] == year:
                film_data.append((line.split("\t")[0],
                                  line.split("\t")[-1][:-1]))
            bar.update(i)
            i += 1
    return film_data


def generate_coordinates(location):
    """
    (str) -> list
    Gets location name and returns list with coordinates
    """
    geolocator = Nominatim(user_agent="web_map")
    geocode = RateLimiter(geolocator.geocode, min_delay_seconds=0.1)
    coordinate = geolocator.geocode(location)
    return [coordinate.latitude, coordinate.longitude]


if __name__ == '__main__':
    mapa_build()
