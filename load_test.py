from locust import HttpUser, TaskSet, task, between

class UserBehavior(TaskSet):
    @task(1)
    def index(self):
        self.client.get("/")

    @task(1)
    def add_user(self):
        self.client.get("/add")

    @task(1)
    def get_user(self):
        self.client.get("/get")

class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(0, 0)  # без задержки между запросами

if __name__ == "__main__":
    import os
    os.system("locust -f load_test.py --host=http://localhost:8180")