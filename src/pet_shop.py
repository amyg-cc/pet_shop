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

def get_pets_by_breed(shop_details, breed):
    breed_list = []
    for pet in shop_details["pets"]:
        if pet["breed"] == breed:
            breed_list.append(pet)
    return breed_list

def find_pet_by_name(shop_details, name):
    for pet in shop_details["pets"]:
        if pet["name"] == name:
            return pet

def remove_pet_by_name(shop_details, name):
    for pet in shop_details["pets"]:
        if pet["name"] == name:
            shop_details["pets"].remove(pet)

def add_pet_to_stock(shop_details, new_pet):
    shop_details["pets"].append(new_pet)

def get_customer_cash(customer):
    return customer["cash"]
