from scrapper import Scrapper
import mysites

amazon = mysites.Amazon()
ml = mysites.ML()


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
    ...

def ask_stores():
    ...

def start_scrapper():
    
    Scrapper()
    
    
def main():
    
    ask_products()
    ask_stores()
    start_scrapper()
    
    
if __name__ == "__main__":
    main()
