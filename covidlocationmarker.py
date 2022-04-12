from kivy_garden.mapview import MapMarkerPopup
from locationpopupmenu import LocationPopupMenu

class CovidLocationMarker(MapMarkerPopup):
    location_data = []
    def on_release(self):
        # Open up the locationPopupMenu
        menu = LocationPopupMenu(self.location_data)
        menu.size_hint = [.8, .9]
        menu.open()