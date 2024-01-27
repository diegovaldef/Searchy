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
    ...

def start_scrapper():
    
    Scrapper()
    
    
def welcome():
    
    print("Welcome!, here some reminders:\n")
    print("- You can only search for a max of 5 products")
    print("- Write 'finish' to complete the writing of products")
    print("(if you don't want 5)\n\n")
    
    
def main():
    
    ask_products()
    ask_stores()
    start_scrapper()
    
    
if __name__ == "__main__":
    main()
