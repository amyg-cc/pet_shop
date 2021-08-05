# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(shop_details):
    return shop_details["name"]

def get_total_cash(shop_details):
    return shop_details["admin"]["total_cash"]

def add_or_remove_cash(shop_details, amount):
    shop_details["admin"]["total_cash"] += amount

def get_pets_sold(shop_details):
    return shop_details["admin"]["pets_sold"]

def increase_pets_sold(shop_details, amount):
    shop_details["admin"]["pets_sold"] += amount

def get_stock_count(shop_details):
    return len(shop_details["pets"])