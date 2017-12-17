from googlemaps import Client as GoogleMaps

class location:
    def __init__(self, s = ""):
        self.api_key = 'AIzaSyAhb_rBwht_tVUC0VEFMiQIqelRESZgL_c'
        if s != "":
            self.api_key = s
        self.gmaps = GoogleMaps(self.api_key)

    def find_location_for(self, adr):
        l = self.gmaps.geocode(adr)
        lat = l[0]["geometry"]["location"]["lat"]
        lon = l[0]["geometry"]["location"]["lng"]
        return lat, lon
