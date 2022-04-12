from kivymd.uix.dialog import ListMDDialog

class LocationPopupMenu(ListMDDialog):
    def __init__(self, location_data):
        super().__init__()
        self.location_data = location_data
        print(location_data)
        # Set all of the fields of covid location data
        headers = "Hospital_name,Phone_number,Street_address,Suburb,Postcode,state,LHN,PHNa,Website,Description,Sector,Beds"
        headers = headers.split(',')
        for i in range(len(headers)):
            attribute_name = headers[i]
            attribute_value = location_data[i]
            setattr(self, attribute_name, attribute_value)