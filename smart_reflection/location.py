from googlemaps import Client as GoogleMaps

class Singleton(type):
    def __init__(cls, name, bases, attrs, **kwargs):
        super().__init__(name, bases, attrs)
        cls._instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance

class location(metaclass=Singleton):
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
