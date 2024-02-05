# Searchy - Web Scraping Tool by Diego Valdes
A simple way to search products on "Amazon" and "Mercado Libre" 
(Currently only works on the Mexican versions)

## What does Searchy do?
Searchy is a web scraping tool designed to search and extract product information from online stores. The tool currently supports two popular stores: Amazon and Mercado Libre (Only on Mexico). It uses the Selenium and Requests_HTML libraries in Python to obtain data from web pages, and generates an Excel file with the search results.

## Features
- Store Support: Searchy currently supports searches in two online stores: Amazon and Mercado Libre.
- Product Limit: You can search up to a maximum of 5 products per run.
- Product Limit per Store: The tool will search up to 100 products for each store and product specified.
- Excel Output: The search results will be saved in an Excel file in the run directory.
- Efficient Search: Searchy uses web scraping techniques to extract relevant information from product pages.

## How to use

### Download and Execution:
Download the Searchy.exe executable file from the project repository.
Run Searchy.exe to start the tool.

### Search Configuration:
Once the tool is started, follow the instructions in the CLI to enter the products you want to search for and select the stores.

### Results:
After completing the search, the tool will generate an Excel file in the same running directory.
The Excel file will contain detailed information about the products found, including title, price, rating and more.

### Results Display:
Upon completion of the search, Searchy will automatically open the Excel file with the results.

## System Requirements
Windows Operating System (to run the Searchy.exe executable file).
Google Chrome in its latest version.
It is not necessary to install additional libraries or have Python installed.

## Important Notes:
Make sure you have permissions to run scripts and have Internet access to perform the searches.
The tool may take some time to complete the search, depending on the number of products and the speed of the Internet connection.

## Details Section

In this section we will explain what each important file does and how it works.

### Project.py

The main file where all functions are grouped together

#### Functions:

- welcome(): Displays welcome messages and reminders about the application's usage.

- input_products(): Takes user input for up to 5 products and checks for a special input, "finish," to stop input.

- input_stores(): Takes user input for whether they want to search on Amazon and/or Mercado Libre.

- check_products(product, products): Checks if the user input is "finish" and if the product list is not empty.

- format_stores(stores): Formats the user's store preferences into a list of site-specific classes from mysites.

- excel_name(products): Generates an Excel file name based on the first product in the list.

- pre_scrapper(): Displays a message before the web scraping process begins.

- post_scrapper(excel_file): Displays a completion message, opens the resulting Excel file, and handles exceptions if the file cannot be opened.

- start_scrapper(products, stores, excel_file): Initiates the web scraping process by creating a Scrapper object with user prompts and opens the resulting Excel file.

### Scrapper.py

The file that does the scrapping of all the data

#### Scrapper Class:

- `__init__`(self, user_prompts): Initializes the scraper with user-provided prompts and sites. Sets up variables, including the Selenium WebDriver, maximum number of products to scrape (max_products), and then calls the execute method.

- execute(self): Iterates through each site and prompt combination. Calls methods to get HTML, parse HTML, and make an Excel file for each combination.

- get_html(self, url): Retrieves HTML content from the specified URL using either Selenium or Requests, depending on the specified method in the site configuration.

- parse_html(self): Parses the HTML content based on the provided XPath expressions in the site configuration and stores the extracted data in the site.elements attribute.

- make_excel(self): Creates a Pandas DataFrame from the extracted elements and concatenates it with the existing DataFrame (if any). The resulting DataFrame is saved as an Excel file.

- start_driver(self): Initializes the Selenium WebDriver if it doesn't exist, and returns the driver.

- exit(self): Cleans up by organizing the final DataFrame, saving it to an Excel file, closing the WebDriver, and closing the progress bar.

#### Pbar class:

- `__init__`(cls, prompts, sites, max_products): Initializes a progress bar using the tqdm library with the total number of iterations calculated based on the number of prompts, sites, and max_products.

- update(cls, number): Updates the progress bar by incrementing the counter and updating the bar.

- close(cls): Closes the progress bar when the scraping process is complete.

#### Overall flow:

The script iterates through each site and prompt combination, fetching HTML content, parsing it to extract relevant information, and updating the progress bar.

The extracted data is stored in a Pandas DataFrame, and the script continues to the next page (if available) until the maximum number of products (max_products) is reached.

After scraping data from all combinations, the final DataFrame is saved to an Excel file, and the WebDriver is closed.

Please note that the code is designed to be modular, making use of classes and methods for better organization and readability. The progress bar is used to provide feedback on the scraping progress.

### Mysites.py

The file that stores the information of the sites in classes

#### Common Base Class: Site

##### Attributes:

- name: Name of the website (e.g., "Amazon", "Mercado Libre").
- url: Base URL for the website.
- html_obteined_with: Specifies the method used to obtain HTML data (e.g., "selenium", "requests").
- sleep_time: A delay time used for scraping to prevent being blocked by the website.
- base_path: XPath expression for the base path of the HTML elements to be scraped.
- paths: Dictionary containing XPath expressions for specific data elements like Title, Price, Stars, Reviews, etc.
- next_page: XPath expression for the link to the next page.
- prefix_next_page: Prefix to be added to the next page link.
- sufix_next_page: Suffix to be added to the next page link.
- last_column: Indicates the last column in the dataset.
- raw_elements: Dictionary to store raw data scraped from the website.
- elements: Dictionary to store processed and formatted data.

##### Methods:

fix_elements(): Processes raw elements and populates the elements dictionary with cleaned and formatted data.
Checks for specific conditions in the raw data and transforms it into a more usable format.
Updates a progress bar (Pbar) to track the number of elements processed.