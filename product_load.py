import csv


def load_products(filename):
    products = []
    with open("prod.csv", "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            products.append(
                {
                    "id": int(row["id"]),
                    "name": row["name"],
                    "price": float(row["price"]),
                    "description": row["description"]
                }
            )
    return products