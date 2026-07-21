import requests


class ApiClient:

    BASE_URL = "https://fakestoreapi.com"

    def get(self, endpoint: str):
        
        url = f"{self.BASE_URL}/{endpoint}"

        try:

            response = requests.get(url, timeout=30)

            response.raise_for_status()

            return response.json()

        except requests.exceptions.RequestException as error:

            raise Exception(f"Erro ao acessar a API: {error}")