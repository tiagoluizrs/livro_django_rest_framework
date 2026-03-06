from locust import HttpUser, TaskSet, task, between


class UserBehavior(TaskSet):
    def on_start(self):
        # Autentica e obtém o token JWT - Coloque seu usuário e senha aqui
        response = self.client.post(
            "/api/v1/token/", json={"username": "usuario", "password": "#Mudar123"}
        )

        # Se a autenticação falhar, mostre o erro no log
        if response.status_code != 200:
            print(f"Falha no login: {response.status_code} - {response.text}")
            return

        token = response.json().get("access")
        self.client.headers.update({"Authorization": f"Bearer {token}"})

    @task(2)
    def listar_categorias(self):
        self.client.get("/api/v1/category/")


class WebsiteUser(HttpUser):
    tasks = [UserBehavior]
    wait_time = between(1, 5)
    host = "http://127.0.0.1:8080"
