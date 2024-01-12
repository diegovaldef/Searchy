from async_scrapper import Scrapper
import mysites

amazon = mysites.Amazon()
ml = mysites.ML()


user_prompts = {
    
    "prompts": [
            
        "Teclado Mecanico",
        "Mouse",
        "Monitor Gamer"
            
    ],    
    
    "sites": [

        amazon,
        ml
        
    ]
    
}

Scrapper(user_prompts)
