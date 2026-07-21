from src.ingestion.products import get_products


def main():
    products = get_products()

    print(f"Quantidade de produtos: {len(products)}")
    print(products[0])


if __name__ == "__main__":
    main()