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
Once the tool is started, follow the instructions in the GUI to enter the products you want to search for and select the stores.

### Results:
After completing the search, the tool will generate an Excel file in the same running directory.
The Excel file will contain detailed information about the products found, including title, price, rating and more.

### Results Display:
Upon completion of the search, Searchy will automatically open the Excel file with the results.

## System Requirements
Windows Operating System (to run the Searchy.exe executable file).
It is not necessary to install additional libraries or have Python installed.

## Important Notes:
Make sure you have permissions to run scripts and have Internet access to perform the searches.
The tool may take some time to complete the search, depending on the number of products and the speed of the Internet connection.