from locust import HttpUser, TaskSet, task, between


class UserBehavior(TaskSet):
    def on_start(self):
        # Autentica e obtém o token JWT
        response = self.client.post(
            "/api/v1/token/", json={"username": "admin", "password": "#Brendhas3v3n"}
        )
        token = response.json().get("access")
        self.client.headers.update({"Authorization": f"Bearer {token}"})

    @task(2)
    def listar_categorias(self):
        self.client.get("/api/v1/category/")

    @task(2)
    def sentry_debug(self):
        self.client.get("/sentry-debug/")


class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(1, 5)
