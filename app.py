from src.services.planets_loader import PlanetsLoader


def main():
    planets_loader = PlanetsLoader()
    planets = planets_loader.get_planets()


if __name__ == '__main__':
    main()

