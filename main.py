import inflect
import sys
from scrapper import Scrapper
import mysites

p = inflect.engine()
amazon = mysites.Amazon()
ml = mysites.ML()


MAX_PRODUCT_QTY = 5

def welcome():
    
    print("-- Harvard CS50P Final Proyect ---- 'Searchy' by Diego Valdes --\n")
    
    print("Welcome!, here are some reminders:\n")
    print("- You can only search for a max of 5 products")
    print("- Write 'finish' to complete the writing of products (if you don't want 5)")
    print("- For each product and store prompted 100 products will be searched at most")
    print("- The results will appear in a Excel file\n")
    
def ask_products():
    
    products = []
    welcome()
    
    while len(products) < MAX_PRODUCT_QTY:
        product = input(f"Write your {p.ordinal(len(products) + 1)} product: ")
        
        if product == "finish":
            
            if len(products) == 0:
                sys.exit("Please write at least one product")
            
            break
        
        products.append(product)
        
    return products
        
def ask_stores():
    
    stores = []
    
    while True:
    
        amazon_store = input("Do you want to search on Amazon? [y/n]: ")
    
        if amazon_store == "y":
            stores.append(amazon)
            break
    
        elif amazon_store == "n":
            break
    
    while True:
        
        ml_store = input("Do you want to search on Mercado Libre [y/n]: ")
        
        if ml_store == "y":
            stores.append(ml) 
            break
    
        elif ml_store == "n":
            break
        
        
    if stores == []:
        sys.exit("Please search at least in one store")
        
        
    return stores
        
def start_scrapper(products, stores):
    
    user_prompts = {
        
        "prompts": [product for product in products],
        "sites": [store for store in stores]
        
    }
    
    print("\nPerfect! Let's start to work")
    print("This may take some minutes")
    
    Scrapper(user_prompts)
    
    print("Done!")
    print("Your Excel file is in this directory")

def main():
    
    products = ask_products()
    stores = ask_stores()
    start_scrapper(products, stores)

if __name__ == "__main__":
    main()
