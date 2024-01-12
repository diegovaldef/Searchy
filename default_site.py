from abc import ABC, abstractmethod

class Site(ABC):
    
    @abstractmethod
    def __init__(self):
        pass
    

    @abstractmethod
    def fix_elements(self):
        pass 
    
