import asyncio
from concurrent.futures import ThreadPoolExecutor
from selenium import webdriver
from requests_html import AsyncHTMLSession
from lxml import html
from time import sleep
from os import system, name as os_name
import pandas as pd

class Scrapper:
        
    def __init__(self, user_prompts):
        
        self.sites = user_prompts["sites"]
        self.prompts = user_prompts["prompts"]
        self.driver = None
        self.execute()
        
    def execute(self):
        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.run_parallel())

    async def run_parallel(self):
        async with ThreadPoolExecutor() as executor:
            await asyncio.gather(*(self.process_site(site) for site in self.sites))

    async def process_site(self, site):
        for prompt in self.prompts:
            await self.process_prompt(site, prompt)

    async def process_prompt(self, site, prompt):
        url = site.url + prompt
        while site.counter < 100:
            page_html = await self.get_html(url, site)
            elements = self.parse_html(page_html, site)
            dataframe = self.make_excel(elements, site, prompt)
            try:
                if isinstance(page_html.xpath(site.next_page), str):
                    url = site.prefix_next_page + page_html.xpath(site.next_page) + site.sufix_next_page
                else:
                    url = site.prefix_next_page + page_html.xpath(site.next_page)[0] + site.sufix_next_page
            except IndexError:
                continue
        site.counter = 0

    async def get_html(self, url, site):
        async with ThreadPoolExecutor() as executor:
            return await asyncio.get_event_loop().run_in_executor(executor, lambda: self._get_html_sync(url, site))

    def _get_html_sync(self, url, site):
        if site.html_obteined_with == "selenium":
            driver = self.start_driver()
            driver.get(url)
            sleep(site.sleep_time)
            page_html = html.fromstring(driver.page_source)
        elif site.html_obteined_with == "requests":
            session = AsyncHTMLSession()
            response = session.get(url)
            html_string = response.html.html
            page_html = html.fromstring(html_string)
        return page_html

    def parse_html(self, page_html, site):
        elements = []
        for selected in page_html.xpath(site.base_path):
            if site.counter < 100:
                for element, path in site.paths.items():
                    site.raw_elements[element] = selected.xpath(path)
                site.fix_elements()
            else:
                break
        return site.elements

    def make_excel(self, elements, site, prompt):
        actual_dataframe = pd.DataFrame(elements)
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
            self.driver = webdriver.Chrome(options=options)
        return self.driver

    def exit(self):
        self.dataframe = self.dataframe[[col for col in self.dataframe.columns if col != self.site.last_column] + [self.site.last_column]]
        self.dataframe.to_excel(f"{self.prompts[0]}.xlsx", index=False)
        if self.driver:
            self.driver.close()
        system("clear" if os_name == "posix" else "cls")
        print("Done!")
