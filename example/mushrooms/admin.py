from leaflet_point.admin import LeafletPointAdmin
from django.contrib import admin

from . import models

# We overwrite the map_settings with config_overrides
# If model had latitude and longitude this isn't necessary!
class CustomLeafletPointAdmin(LeafletPointAdmin):
	list_display = ('title', 'lat', 'lng')

admin.site.register(
	models.MushroomSpot, 
	LeafletPointAdmin, 
	config_overrides = {
        'lat_input_selector': 'lat', # defaults to latitude
    	'lng_input_selector': 'lng', # defaults to longitude
    	'geocoder': True # defaults to false
    }   
)