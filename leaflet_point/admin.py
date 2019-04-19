from django.conf import settings
from django.contrib.admin import ModelAdmin

# Fetch global settings from settings.py
LEAFLET_POINT_CONFIG = getattr(settings, 'LEAFLET_POINT_CONFIG', {})

# Default settingsleaflet_point_config
# Question for future: Should this be here?
LEAFLET_POINT_CONFIG = dict({
    # Selectors
    'lat_input_selector': 'latitude',
    'lng_input_selector': 'longitude',
    # Style
    'map_height': 400,
    # Leaflet
    'tile_layer': 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',
    'attribution': '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
    'initial_lat': 51.4825766, ## Greenwich
    'initial_lng': 0, ## Greenwich
    'initial_zoom': 15,
    'min_zoom': 0,
    'max_zoom': 19,
    'max_zoom_tilelayer': 19,
    'geocoder': False,
}, **LEAFLET_POINT_CONFIG)

class LeafletPointAdmin(ModelAdmin):

    change_form_template = 'leaflet_point/admin/change_form.html'
    config_overrides = {}

    def add_view(self, request, form_url='', extra_context= {}, leaflet_point_config=LEAFLET_POINT_CONFIG):
        leaflet_point_config.update(extra_context)
        leaflet_point_config.update(self.config_overrides)
        return super().add_view(
            request, form_url, extra_context=leaflet_point_config,
        )

    def change_view(self, request, object_id, form_url='', extra_context = {}, leaflet_point_config=LEAFLET_POINT_CONFIG):
        leaflet_point_config.update(extra_context)
        leaflet_point_config.update(self.config_overrides)
        return super().change_view(
            request, object_id, form_url, extra_context=leaflet_point_config,
        )

    class Media:
        css = {
            'all': (
                'leaflet_point/leaflet.css',
                'leaflet_point/Control.Geocoder.css',
            )
        }
        js = (
            'leaflet_point/leaflet.js',
            'leaflet_point/Control.Geocoder.js',
        )