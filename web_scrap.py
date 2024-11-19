from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from bs4 import BeautifulSoup
import time

def call_website(product_name):
    # Set up the Edge driver
    product_name=product_name.replace(" ","%20")
    driver_path = r"C:\Users\sakth\Downloads\msedgedriver.exe"
    service = Service(driver_path)
    options = Options()
    options.use_chromium = True  # Ensure Chromium-based Edge is used
    options.add_argument('--headless')  # Run in headless mode
    options.add_argument('--disable-gpu')  # Disable GPU acceleration
    driver = webdriver.Edge(service=service, options=options)
    # Open the URL
    url = f"https://pricee.com//?q={product_name}"
    print(url)
    driver.get(url)
    # Wait for the page to load
    time.sleep(5)
    # Get page source and parse with BeautifulSoup
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    # Extract the desired elements
    elements = soup.find('div', class_='wtb-container pricee-cntnr').find_all('ul',id='wheretobuy')
    # Close the browser
  
    # for ele in elements:
    #     tags=ele.find_all('li',class_='ng-scope') 
    # print(tags)
    # print('-'*20)    
    for val in elements:
        price=val.find_all('div',class_='pd-detail tbl-col')
    driver.quit()
    return price
