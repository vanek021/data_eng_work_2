import json
import pickle

def update_price(product, price_info):
    method = price_info["method"]
    if method == "add":
        product["price"] += price_info["param"]
    elif method == "sub":
        product["price"] -= price_info["param"]
    elif method == "percent+":
        product["price"] *= (1 + price_info["param"])
    elif method == "percent-":
        product["price"] *= (1 - price_info["param"])

with open("./task4/price_info_29.json", "r") as f:
    price_info_json = json.load(f)

    with open("./task4/products_29.pkl", "rb") as f_p:
        product_json = pickle.load(f_p)

        price_info = dict()
        products = dict()

        for item in price_info_json:
            price_info[item["name"]] = item

        for item in product_json:
            products[item["name"]] = item

        for name, data in price_info.items():
            if name in products:
                update_price(products[name], data)

        result = list(products.values())

        with open("./task4/products_result.pkl", "wb") as r_p:
            r_p.write(pickle.dumps(result))
    