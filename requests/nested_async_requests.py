from httpx import AsyncClient
from pokes import pokes
import asyncio


async def main(pokemon: str) -> None:
    print(f"Entrada: {pokemon}")
    async with AsyncClient(
        base_url="https://pokeapi.co/api/v2",
        timeout=None
    ) as client:
        response = await client.get(f'/pokemon/{pokemon}')
        result = response.json()
        _id = result.get("id")

        response = await client.get(f'/pokemon-species/{_id}')
        result = response.json()
        evolution_chain_url = result.get('evolution_chain', {}).get('url')

        response = await client.get(evolution_chain_url)
        result = response.json()
        for poke in result.get('chain', {}).get('evolves_to', []):
            print(f"{pokemon} -> {poke.get('species', {}).get('name')}")


async def run_tasks():
    tasks = [main(poke) for poke in pokes]
    await asyncio.gather(*tasks)

if __name__ == '__main__':
    asyncio.run(run_tasks())
