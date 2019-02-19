from pymongo import MongoClient

from src.domain.entities.planet import Planet


class PlanetRepository(object):

    def insert_list(self, planets: list):
        print("conectado no mongo")
        client = MongoClient('mongodb://localhost:27017/')
        print("conectado no banco")
        database = client['b2w-database']
        print("conectado na colecao")
        collection = database['pĺanet-collection']

        for planet in planets:
            print("adicionado " + planet.name)
            self.insert(planet, collection)

    def insert(self, planet: Planet, collection):
        planet_scheme = {
            "name": planet.name,
            "terrain": planet.terrain,
            "climate": planet.climate
        }

        collection.insert_one(planet_scheme)
