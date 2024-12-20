from locust import User, task, between


class LoadTesting(User):
    @task
    def load_test_task(self):
        print("executing my_task")

    wait_time = between(0.5, 10)
