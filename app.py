from src.repositories.planet_repository import PlanetRepository
from src.services.planets_loader import PlanetsLoader

def main():
    planets_loader = PlanetsLoader()
    planet_repository = PlanetRepository()

    print("obtendo planetas")
    planets = planets_loader.get_planets()

    print("inserindo planetas")
    planet_repository.insert_list(planets)


if __name__ == '__main__':
    main()

