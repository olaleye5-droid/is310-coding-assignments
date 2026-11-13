# GETting Culture Across APIs: Pokémon

## Research Question

How do a community-maintained Pokémon wiki and a structured Pokémon API organize and represent information about the same Pokémon?

## Project Overview

This project explores two different APIs that provide information about Pokémon: the Bulbapedia MediaWiki Action API and PokéAPI. Although both APIs provide information about the Pokémon universe, they organize and present information differently.

The goal is to compare how community-created knowledge and structured database information represent the same cultural subject.

## API 1: Bulbapedia MediaWiki Action API

**Website:** https://bulbapedia.bulbagarden.net/

**API endpoint:** https://pokemon.fandom.com/api.php

Bulbapedia is a community-maintained Pokémon encyclopedia. Its MediaWiki Action API allows users to search wiki pages and retrieve information about articles.

The project uses the `action=query` and `list=search` parameters to search for Pikachu.

The returned information includes:
- Article titles
- Page IDs
- Word counts
- Page sizes
- Revision timestamps

The API returned 10 search results for Pikachu.

## API 2: PokéAPI

**Website:** https://pokeapi.co/

**Endpoint:** https://pokeapi.co/api/v2/pokemon/pikachu

PokéAPI provides structured Pokémon information through a REST API. Unlike a community wiki, it returns standardized data in JSON format.

The project collected:
- Pokémon name
- Height
- Weight
- Types
- Abilities
- Base stats

For Pikachu, the API returned the Electric type and the abilities Static and Lightning Rod.

## Connecting the Two APIs

The project connects the two APIs by searching for Pikachu in Bulbapedia and retrieving Pikachu's structured record from PokéAPI.

The Python program compares the Bulbapedia article title with the PokéAPI Pokémon name. It found an exact match between the wiki title "Pikachu" and the API name "pikachu".

The program stores the results from both APIs and the matching information in `pokemon_api_data.json`.

## Comparing the APIs

The two APIs provide different approaches to organizing cultural information.

Bulbapedia is designed around community-maintained articles. Its search results provide article titles, page IDs, word counts, and timestamps. This structure reflects an encyclopedia where information is organized into pages that people can read, edit, and expand.

PokéAPI is designed around structured data. It provides standardized fields such as height, weight, types, abilities, and statistics. This makes the information easier for software applications to process and compare.

The difference demonstrates how the purpose and intended users of an API influence the way information is organized. Bulbapedia supports browsing and contributing to community knowledge, while PokéAPI supports retrieving consistent data for applications and analysis.

## Files

- `getting_culture.py`: Python program that accesses both APIs, connects their results, and handles errors.
- `pokemon_api_data.json`: Combined data retrieved from both APIs.

## Tools and Libraries

- Python
- Requests
- JSON
- Bulbapedia MediaWiki Action API
- PokéAPI

## Limitations

This project focuses on one Pokémon, Pikachu. The comparison is therefore a small demonstration rather than a complete analysis of either API.

The Bulbapedia API search results provide article metadata rather than the full article text. PokéAPI provides structured game-related data, but it does not provide the same type of community-written descriptions.

The matching process uses an exact title comparison. Differences in spelling, punctuation, or naming conventions could prevent other records from matching even when they refer to the same subject.

## Ethical Considerations

The project makes a limited number of API requests for educational purposes. It does not attempt to bypass access restrictions or collect unnecessary personal information. The results retain the source information for both APIs.
