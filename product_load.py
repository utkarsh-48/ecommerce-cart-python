import csv

def load_products(filename):
    products = []
    try:
        with open(filename, "r") as f:
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
    except FileNotFoundError:
        print(f"Product file '{filename}' not found.")
    except Exception as e:
        print(f"Error loading products: {e}")
    return products