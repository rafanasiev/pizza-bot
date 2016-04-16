import googlemaps

class Places(object):
    ''' Find pizza place'''
    def __init__(self):
        self.key = 'AIzaSyAF2BEoD4kzVJjwP0LRFvehCENLQ_Oueb8'
        self.location = (50.401699,30.2525049)
        self.radius = 100
        self.type = 'meal_delivery'
        self.language = 'en-US'
        self.client = googlemaps.Client(self.key, timeout=300)


    def find_pizza(self, arg):
        result = self.client.places(arg, location=self.location, radius=self.radius, language=self.language, open_now=True)
        return result['results'][0]