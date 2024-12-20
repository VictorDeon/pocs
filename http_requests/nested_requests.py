from httpx import Client
from pokes import pokes


def main(pokemon: str) -> None:
    with Client(base_url="https://pokeapi.co/api/v2", timeout=5.0) as client:
        print(f"Pokemon: {pokemon}")
        response = client.get(f'/pokemon/{pokemon}')
        result = response.json()
        _id = result.get("id")

        response = client.get(f'/pokemon-species/{_id}')
        result = response.json()
        evolution_chain_url = result.get('evolution_chain', {}).get('url')

        response = client.get(evolution_chain_url)
        result = response.json()
        for poke in result.get('chain', {}).get('evolves_to', []):
            print(f"{pokemon} -> {poke.get('species', {}).get('name')}")


if __name__ == '__main__':
    for poke in pokes:
        main(poke)
