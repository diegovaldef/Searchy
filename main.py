from scrapper import Scrapper
import inflect
import mysites

amazon = mysites.Amazon()
ml = mysites.ML()
p = inflect.engine()

MAX_PRODUCT_QTY = 5

# user_prompts = {
    
#     "prompts": [
            
#         "Teclado Mecanico",
#         "Mouse",
#         "Monitor Gamer"
            
#     ],    
    
#     "sites": [

#         amazon,
#         ml
        
#     ]
    
# }

def welcome():
    
    print("Welcome!, here some reminders:\n")
    print("- You can only search for a max of 5 products")
    print("- Write 'finish' to complete the writing of products")
    print("(if you don't want 5)\n\n")
    
def ask_products():
    
    products = []
    welcome()
    
    while len(products) < MAX_PRODUCT_QTY:
        product = input(f"Write your {p.ordinal(len(products))} product")
        
        if product == "finish":
            break
        
        products.append(product)
        
    return products
        
def ask_stores():
    
    stores = []
    
    while True:
    
        amazon_store = input("Do you want to search on Amazon? [y/n]")
    
        if amazon_store == "y":
            stores.append(amazon)
            break
    
        elif amazon_store == "n":
            break
    
    while True:
        
        ml_store = input("Do you want to search on Mercado Libre [y/n]")
        
        if ml_store == "y":
            stores.append(ml) 
            break
    
        elif ml_store == "n":
            break
        
    return stores
        
def start_scrapper(products, stores):
    
    user_prompts = {
        
        "prompts": [product for product in products],
        "sites": [store for store in stores]
        
    }
    
    Scrapper(user_prompts)
    

def main():
    
    products = ask_products()
    stores = ask_stores()
    start_scrapper(products, stores)
    
    
if __name__ == "__main__":
    main()
