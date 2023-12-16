# Enjoy this Toddomation

import aristaCvq as arista
import json
from icecream import ic


def main():
    # We first need to login and get the Cookie for other API call
    cookie = arista.getCookie()
    ic(cookie)

    # This will show the session data based on the API Key that was used
    session = arista.getSession(cookie)
    # ic(session)

    # This will show the complete Location heirarchy for your Arista deployment
    locations = arista.getLocations(cookie)
    # ic(locations)

    # This will write the heirarchy to JSON in case you want more specific data
    with open("CV-CUE/aristaLoctions.json", "w") as file:
        json.dump(locations, file, indent=4)

    # This will show the APs that are assigned (Paged)
    aristaAps = arista.getAps(cookie)
    # ic(aristaAps)

    # This will write all AP data to a JSON file
    with open("CV-CUE/aristaAps.json", "w") as file:
        json.dump(aristaAps, file, indent=4)

    # This will show the clients connected to your Arista network
    aristaClients = arista.getClients(cookie)
    # ic(aristaClients)

    # This will write all Client data to a JSON file
    with open("CV-CUE/aristaClients.json", "w") as file:
        json.dump(aristaClients, file, indent=4)


if __name__ == "__main__":
    main()
