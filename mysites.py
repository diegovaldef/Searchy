from default_site import Site
from re import search

class Amazon(Site):
    def __init__(self):
        self.name = "Amazon"
        self.url = "https://amazon.com.mx/s?k="
        self.html_obteined_with = "selenium"
        self.sleep_time = 2
        self.base_path = '//div[contains(@data-cel-widget, "search_result_")]'
        self.paths = {
            "Title": './/span[@class="a-size-base-plus a-color-base a-text-normal"]/text()',
            "Title_Promotion": './/span[@class="a-size-medium a-color-base a-text-normal"]/text()',
            "Price": './/span[@class="a-price-whole"]/text()',
            "Stars": '//div[@class="a-section a-spacing-none a-spacing-top-micro"]//span[@class="a-icon-alt"]/text()',
            "Reviews": './/span[@class="a-size-base s-underline-text"]/text()',
            "Free_Shipping": './/span[contains(text(), "GRATIS")]',
            "Prime": './/i[@class="a-icon a-icon-prime a-icon-medium"]/@class',
            "Link": './/@data-asin',
            
        }
        self.next_page = '//a[@class="s-pagination-item s-pagination-next s-pagination-button s-pagination-separator"]/@href'
        self.prefix_next_page = 'https://amazon.com.mx'
        self.sufix_next_page = ''
        
        self.last_column = "Link"
        
        self.raw_elements = {}
        self.elements = {
            
            "Title": [],
            "Price": [],
            "Rating": [],
            "Reviews": [],
            "Free_Shipping": [],
            "Prime": [],
            "Link": []
            
        }
        
        self.counter = 0

    def fix_elements(self):
        
        if (
            self.raw_elements["Title"]
            and self.raw_elements["Price"]
            and self.raw_elements["Stars"]
            and self.raw_elements["Reviews"]
        ):

            self.elements["Title"].append(self.raw_elements["Title"][0])
            self.elements["Price"].append(int(self.raw_elements["Price"][0].replace(",","")))

            match = search(r"^([0-5]{1}\.[0-9]{1})", self.raw_elements["Stars"][0])
            rating = round(float(match.group(1)) / 5 * 100)       
            self.elements["Rating"].append(rating)

            self.elements["Reviews"].append(int(self.raw_elements["Reviews"][0].replace(",", "")))
            self.elements["Free_Shipping"].append("YES" if bool(self.raw_elements["Free_Shipping"]) else "NO")
            self.elements["Prime"].append("YES" if bool(self.raw_elements["Prime"]) else "NO")
            self.elements["Link"].append(f"https://www.amazon.com.mx/dp/{self.raw_elements["Link"][0]}")

            self.counter += 1

        elif (self.raw_elements["Title_Promotion"]
            and self.raw_elements["Price"]
            and self.raw_elements["Stars"]
            and self.raw_elements["Reviews"]
            
        ):
            
            self.elements["Title"].append(self.raw_elements["Title_Promotion"][0])
            self.elements["Price"].append(int(self.raw_elements["Price"][0].replace(",","")))

            match = search(r"^([0-5]{1}\.[0-9]{1})", self.raw_elements["Stars"][0])
            rating = round(float(match.group(1)) / 5 * 100)       
            self.elements["Rating"].append(rating)

            self.elements["Reviews"].append(int(self.raw_elements["Reviews"][0].replace(",","")))
            self.elements["Free_Shipping"].append("YES" if bool(self.raw_elements["Free_Shipping"]) else "NO")
            self.elements["Prime"].append("YES" if bool(self.raw_elements["Prime"]) else "NO")
            self.elements["Link"].append(f"https://www.amazon.com.mx/dp/{self.raw_elements["Link"][0]}")

            self.counter += 1

class ML(Site):
    
    def __init__(self):
        
        self.name = "Mercado Libre"
        self.url = "https://listado.mercadolibre.com.mx/"
        self.html_obteined_with = "requests"
        self.base_path = '//div[@class="ui-search-result__wrapper"]'
        self.paths = {

            "Title": './/h2[@class="ui-search-item__title"]/text()',
            "Price": './/span[@class="andes-money-amount ui-search-price__part ui-search-price__part--medium andes-money-amount--cents-superscript"]//span[@class="andes-money-amount__fraction"]/text()',
            "Rating": './/span[@class="ui-search-reviews__rating-number"]/text()',
            "Reviews": './/span[@class="ui-search-reviews__amount"]/text()',
            "Free_Shipping": './/span[@class="ui-pb-highlight"]',
            "Full": './/span[@class="ui-pb-label"]',
            "Link": './/a[@class="ui-search-item__group__element ui-search-link__title-card ui-search-link"]/@href',
            
        }
        self.next_page = '//a[@class="andes-pagination__link ui-search-link"][@title="Siguiente"]/@href'
        self.prefix_next_page = ''
        self.sufix_next_page = ''
        
        self.last_column = "Link"
        self.column_of_links = "Link"

        self.raw_elements = {}
        self.elements = {
            
            "Title": [],
            "Price": [],
            "Rating": [],
            "Reviews": [],
            "Free_Shipping": [],
            "Full": [],
            "Link": []

        }
        
        self.counter = 0
    
    
    def fix_elements(self):
        
        if  (
            self.raw_elements["Title"]
            and self.raw_elements["Price"]
            and self.raw_elements["Rating"]
            and self.raw_elements["Reviews"]
        ):
            
            self.elements["Title"].append(self.raw_elements["Title"][0])
            self.elements["Price"].append(int(self.raw_elements["Price"][0].replace(",", "")))
            self.elements["Rating"].append(round(float(self.raw_elements["Rating"][0]) / 5 * 100))
            
            match = search(r"^\(([0-9]+)\)$", self.raw_elements["Reviews"][0])
            self.elements["Reviews"].append(int(match.group(1)))

            self.elements["Free_Shipping"].append("YES" if bool(self.raw_elements["Free_Shipping"]) else "NO")
            self.elements["Full"].append("YES" if bool(self.raw_elements["Full"]) else "NO" )
            self.elements["Link"].append(self.raw_elements["Link"][0])
            
            self.counter += 1