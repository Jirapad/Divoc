from kivymd.app import MDApp
from kivy.core.window import Window
import sqlite3
from searchpopupmenu import SearchPopupMenu

from covidlocationsmapview import CovidLocationsMapView

Window.size = (375, 750)

class MainApp(MDApp):
    connection = None
    cursor = None
    search_menu = None
    def on_start(self):
        # Initialize GPS

        # Connect to database
        self.connection = sqlite3.connect("allhospitals.db")
        self.cursor = self.connection.cursor()

        # Instantiate SearchPopupMenu
        self.search_menu = SearchPopupMenu()


MainApp().run()

