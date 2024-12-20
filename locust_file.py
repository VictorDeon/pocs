from locust import User, task, between
import asyncio
from http_requests.async_request import run_tasks


class LoadTesting(User):
    @task
    def load_test_task(self):
        asyncio.run(run_tasks(10))

    wait_time = between(1, 3)
