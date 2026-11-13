
import requests
import json
import time

# API endpoints
WIKI_URL = "https://pokemon.fandom.com/api.php"
POKEAPI_URL = "https://pokeapi.co/api/v2/pokemon/pikachu"

HEADERS = {
    "User-Agent": "IS310StudentResearch/1.0 (educational coursework)"
}


def get_wiki_data(pokemon_name):
    """Search the Pokémon community wiki."""

    params = {
        "action": "query",
        "list": "search",
        "srsearch": pokemon_name,
        "srlimit": 10,
        "format": "json"
    }

    response = requests.get(
        WIKI_URL,
        params=params,
        headers=HEADERS,
        timeout=20
    )

    response.raise_for_status()

    data = response.json()

    return data["query"]["search"]


def get_pokemon_data(pokemon_name):
    """Retrieve structured Pokémon information from PokéAPI."""

    response = requests.get(
        f"{POKEAPI_URL.rsplit('/', 1)[0]}/{pokemon_name.lower()}",
        timeout=20
    )

    response.raise_for_status()

    data = response.json()

    return {
        "name": data["name"],
        "height": data["height"],
        "weight": data["weight"],
        "types": [
            item["type"]["name"]
            for item in data["types"]
        ],
        "abilities": [
            item["ability"]["name"]
            for item in data["abilities"]
        ],
        "stats": {
            item["stat"]["name"]: item["base_stat"]
            for item in data["stats"]
        }
    }


def main():

    pokemon_name = "pikachu"

    print("Connecting to the Pokémon Wiki API...")

    try:
        wiki_results = get_wiki_data(pokemon_name)

        print("\nWiki search results:")

        for result in wiki_results:
            print("-", result["title"])

        time.sleep(1)

        print("\nConnecting to PokéAPI...")

        pokemon_data = get_pokemon_data(pokemon_name)

        print("\nPokéAPI results:")
        print("Name:", pokemon_data["name"])
        print("Types:", pokemon_data["types"])
        print("Abilities:", pokemon_data["abilities"])

        # Connect the two APIs by matching Pokémon names
        wiki_match = next(
            (
                result for result in wiki_results
                if result["title"].lower() == pokemon_name
            ),
            None
        )

        combined_data = {
            "research_subject": pokemon_name,
            "wiki_api": {
                "source": WIKI_URL,
                "results": wiki_results
            },
            "pokeapi": {
                "source": POKEAPI_URL,
                "pokemon": pokemon_data
            },
            "connection": {
                "matched": wiki_match is not None,
                "matching_wiki_title": (
                    wiki_match["title"] if wiki_match else None
                )
            }
        }

        with open(
            "pokemon_api_data.json",
            "w",
            encoding="utf-8"
        ) as file:
            json.dump(
                combined_data,
                file,
                indent=4,
                ensure_ascii=False
            )

        print("\nConnection between APIs:")
        print("Matching wiki page:", combined_data["connection"]["matching_wiki_title"])
        print("Match found:", combined_data["connection"]["matched"])

        print("\nFinished! Data saved to pokemon_api_data.json")

    except requests.RequestException as error:
        print("API request error:", error)

    except (ValueError, KeyError) as error:
        print("Data processing error:", error)


if __name__ == "__main__":
    main()
