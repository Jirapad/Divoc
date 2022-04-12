from kivy.clock import Clock
from kivy.app import App
from kivy_garden.mapview import MapView
from covidlocationmarker import CovidLocationMarker

class CovidLocationsMapView(MapView):
    getting_covidlocations_timer = None
    location_names = []
    def start_getting_covidlocations_in_fov(self):
        # After one sec, get the markets in the field of view
        try:
            self.getting_covidlocations_timer.cancel()
        except:
            pass
        self.getting_covidlocations_timer = Clock.schedule_once(self.get_covidlocations_in_fov, 1)

    def get_covidlocations_in_fov(self, *args):
        # Get reference to main app and the database cursor
        min_lat, min_lon, max_lat, max_lon = self.get_bbox()
        app = App.get_running_app()
        sql_statement = "SELECT * from hospitals WHERE x > %s AND x < %s AND y > %s AND y < %s" % (min_lat, max_lat, min_lon, max_lon)
        print(self.get_bbox())
        app.cursor.execute(sql_statement)
        locations = app.cursor.fetchall()
        print(f"Min lat: {min_lat}, Max lat: {max_lat}, Min lon: {min_lon}, Max lon: {max_lon}")
        print(locations)

        for location in locations:
            name = location[0]
            if name in self.location_names:
                continue
            else:
                self.add_covidlocation(location)

    def add_covidlocation(self, location):
        # Create the CovidLocationMarker
        lat, lon = location[12], location[13]
        marker = CovidLocationMarker(lat=lat, lon=lon)
        marker.source = "alarm.png"

        # Initialize variables
        marker.location_data = location

        # Add the CovidLocationMarker to the map
        self.add_widget(marker)

        # Keep track of the CovidLocation's name
        name = location[0]
        self.location_names.append(name)
