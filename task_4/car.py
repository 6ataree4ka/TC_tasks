class Car(object):

    def __init__(self, brand, model, year, engines, transmissions):
        self.brand = brand
        self.model = model
        self.year = year
        self.engines = engines
        self.transmissions = transmissions

    def __str__(self):
        print("brand =", self.brand, ",", "model =", self.model, ",", "year =", self.year, ",",
              "engines =", self.engines, ",", "transmissions =", self.transmissions)
