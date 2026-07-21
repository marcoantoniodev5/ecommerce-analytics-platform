from src.ingestion.client import ApiClient


def get_products():

    client = ApiClient()

    products = client.get("products")

    return products