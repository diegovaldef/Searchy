import inflect
import sys
from time import sleep
import subprocess

from scrapper import Scrapper
import mysites

p = inflect.engine()

MAX_PRODUCT_QTY = 5

def welcome():
    
    print("-- Harvard CS50P Final Proyect ---- 'Searchy' by Diego Valdes --\n")
    
    print("Welcome!, here are some reminders:\n")
    print("- You can only search for a max of 5 products")
    print("- Write 'finish' to complete the writing of products (if you don't want 5)")
    print("- For each product and store prompted 100 products will be searched at most")
    print("- The results will appear in a Excel file\n")
 
def input_products():
    
    products = []
    
    while len(products) < MAX_PRODUCT_QTY:
        
        product = input(f"Write your {p.ordinal(len(products) + 1)} product: ")
        
        if check_products(product, products): break
        
        products.append(product)
    
    return products
    
def input_stores():
    
    stores = {}
    
    while True:
        amazon_store = input("Do you want to search on Amazon? [y/n]: ")
        
        if amazon_store in ["y", "n"]:
            stores["amazon"] = amazon_store
            break
        
    
    while True:
        ml_store = input("Do you want to search on Mercado Libre [y/n]: ")
        
        if ml_store in ["y", "n"]:
            stores["ml"] = ml_store
            break

    return stores
    
def check_products(product, products):
    
    if product == "finish":
        
        if len(products) == 0:
            sys.exit("Please write at least one product")
            
        return True    
        
    return False
    

def format_stores(stores):
    
    formated_stores = []
    
    if set(stores) == "n":
        sys.exit("Please search at least in one store")

    if stores["amazon"] == "y": 
        formated_stores.append(mysites.Amazon())
    
    if stores["ml"] == "y":
        formated_stores.append(mysites.ML())
        
    return formated_stores
    
def excel_name(products):
    
    excel_file = f"{products[0]}.xlsx"
    return excel_file
    
def pre_scrapper():
    
    print("\nPerfect! Let's start to work")
    sleep(0.5)

def post_scrapper(excel_file):
    
    print("Done!")
    print("Your Excel file is in the same directory as the executable")
    sleep(2)
    print("Opening the results...")
    sleep(2)
    
    try:
        subprocess.Popen(['start', 'excel', excel_file], shell=True)

    except Exception:
        return False
    
    return True       

def start_scrapper(products, stores, excel_file):
    
    user_prompts = {
        
        "prompts": [product for product in products],
        "sites": [store for store in stores]
        
    }
    
    pre_scrapper()
    Scrapper(user_prompts)
    
    if not post_scrapper(excel_file):
        sys.exit("No se pudo abrir el archivo Excel")
    
def main():
    
    welcome()
    
    products = input_products()
    excel_file = excel_name(products)
    
    stores = input_stores()
    stores = format_stores(stores)
    
    start_scrapper(products, stores, excel_file)

if __name__ == "__main__":
    main()
