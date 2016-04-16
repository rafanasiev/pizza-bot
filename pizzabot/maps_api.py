from dbh import PizzaBotDB
try:
    import googlemaps
except ImportError:
    raise  ImportError('googlemaps module not installed')

FIELDS = ['id', 'name', 'international_phone_number', 'place_id', 'rating']

class Places(object):
    ''' Find pizza place'''
    def __init__(self):
        self.key = 'AIzaSyAF2BEoD4kzVJjwP0LRFvehCENLQ_Oueb8'
        self.location = (50.401699, 30.2525049)
        self.radius = 100
        self.type = 'meal_delivery'
        self.language = 'en-US'
        self.client = googlemaps.Client(self.key, timeout=300)
        self.action = "order pizza"

    def find_pizza(self, args):
        print " >>> Got args: %s" % (' '.join(args))
        all_results = self.client.places(self.action, location=self.location, radius=self.radius, language=self.language, open_now=True)
        best_pizza = all_results['results'][0]['place_id']
        result = self.client.place(best_pizza)
        db = PizzaBotDB()
        db.insert(result)
        final_dict = {}

        for f in FIELDS:
            if result['result'].has_key(f):
                print " %s => %s" % (f, result['result'][f])
                final_dict[f] = result['result'][f]
            else:
                final_dict[f] = None

        return final_dict
