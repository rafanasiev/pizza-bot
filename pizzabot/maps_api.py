import googlemaps

FIELDS = ['id', 'name', 'international_phone_number', 'place_id', 'rating']

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
        all_results = self.client.places(arg, location=self.location, radius=self.radius, language=self.language, open_now=True)
        best_pizza = all_results['results'][0]['place_id']
        result = self.client.place(best_pizza)
        print result
        final_dict = {}
        for f in FIELDS:
            final_dict[f] = result['result'][f]
            print result['result'][f]
        return final_dict