import httpx
import asyncio
from aiometer import run_all
from functools import partial

TOTAL_REQUEST = 10
TIMEOUT = None


async def fetch(i: int, client: httpx.AsyncClient) -> None:
    print(f"Iniciando requisição {i}")
    await client.post('/post', json={"code": i})
    print(f"Finalizando requisição {i}")


async def run_tasks(max_per_second: int = 10):
    async with httpx.AsyncClient(
        base_url="https://httpbin.org",
        headers={"trace_id": "abcd1234"},
        timeout=TIMEOUT
    ) as client:
        # partial junta o método main com o parâmetro poke
        tasks = [partial(fetch, i, client) for i in range(TOTAL_REQUEST)]
        # max_at_once: 5 por vez
        # max_per_second: 10 por segundo
        await run_all(tasks, max_per_second=max_per_second)


if __name__ == '__main__':
    asyncio.run(run_tasks(20))
