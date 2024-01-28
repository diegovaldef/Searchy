from selenium import webdriver
from requests_html import HTMLSession
from lxml import html
from time import sleep
from tqdm import tqdm
from os import system, name as os_name
import pandas as pd

class Scrapper:
        
    def __init__(self, user_prompts):
        
        self.sites = user_prompts["sites"]
        self.prompts = user_prompts["prompts"]
        
        self.driver = None
       
        self.execute()
        
    def execute(self):
        
        for site in self.sites:
            self.site = site
            prompts = len(self.prompts)

            for prompt in range(prompts):

                self.product = self.prompts[prompt]
                url = self.site.url + self.product
                
                while self.site.counter < 100:
                
                    self.html = self.get_html(url)
                    self.elements = self.parse_html()
                    self.dataframe = self.make_excel()

                    try:
                        
                        if isinstance(self.html.xpath(self.site.next_page), str):
                            url = self.site.prefix_next_page + self.html.xpath(self.site.next_page) + self.site.sufix_next_page
                            
                        else:
                            url = self.site.prefix_next_page + self.html.xpath(self.site.next_page)[0] + self.site.sufix_next_page
                        
                    except IndexError:
                        continue                    
                        
                self.site.counter = 0
            
        self.exit()
    
    def get_html(self, url):
    
        match self.site.html_obteined_with:
            
            case "selenium":
                
                while True:
                
                    driver = self.start_driver()
                    driver.get(url)
                    sleep(self.site.sleep_time)
                    page_html = html.fromstring(driver.page_source)
                    
                    if page_html is not None:
                        return page_html
                
                
            case "requests":

                while True:

                    session = HTMLSession()
                    response = session.get(url)
                    html_string = response.html.html
                    page_html = html.fromstring(html_string)
                    
                    if page_html is not None:
                        return page_html

    def parse_html(self):

        for selected in self.html.xpath(self.site.base_path):
            
            if self.site.counter < 100:
            
                for element, path in self.site.paths.items():
                        
                    self.site.raw_elements[element] = selected.xpath(path)
                
                self.site.fix_elements()
                
            else:
                break
            
        return self.site.elements
    
    def make_excel(self):
        
        actual_dataframe = pd.DataFrame(self.elements)
        
        try:
            dataframe = pd.concat([self.dataframe, actual_dataframe], ignore_index=True)
            
        except AttributeError:
            
            dataframe = pd.DataFrame()
            dataframe = pd.concat([dataframe, actual_dataframe], ignore_index=True)
        
        dataframe = dataframe.drop_duplicates()
        
        return dataframe
            
    def start_driver(self):
        
        if not self.driver:
            
            options = webdriver.ChromeOptions()
            options.add_argument("--headless")
            options.add_argument("log-level=3") 
                        
            self.driver = webdriver.Chrome(options=options)            
                        
        return self.driver 

    def exit(self):
        
        self.dataframe = self.dataframe[[col for col in self.dataframe.columns if col != self.site.last_column] + [self.site.last_column]]
        self.dataframe.to_excel(f"{self.prompts[0]}.xlsx", index = False)
        
        if self.driver:
            self.driver.close()
            
        system("clear" if os_name == "posix" else "cls")