import json
import http.client

from src.domain.entities.planet import Planet


class PlanetsLoader(object):

    def get_planets(self):
        conn = http.client.HTTPSConnection("swapi.co")

        planets = list()
        page_index = 1

        while True:
            conn.request("GET", "/api/planets/?page=" + str(page_index))

            response = conn.getresponse()

            string = response.read().decode('utf-8')
            json_obj = json.loads(string)

            planets.extend([Planet(name=result["name"], terrain=result["terrain"], climate=result["climate"]) for result in
                       json_obj["results"]])

            if json_obj["next"]:
                page_index = page_index + 1
            else:
                break


        return planets
