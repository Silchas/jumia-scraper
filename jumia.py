import requests
from bs4 import BeautifulSoup
import csv

data = []
page = 1
while page != 6:
    url = f'https://www.jumia.co.ke/mlp-top-deals/?page={page}'
    page = page + 1
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    products = soup.find_all('article', class_='prd _fb _p col c-prd')

    for product in products:
        product_name = product.find('h3', class_='name').text.strip()
        
        price_element = product.find('div', class_='prc')
        price = price_element.text.strip() if price_element else None
        
        discount_element = product.find('div', class_='bdg _dsct _sm')
        discount = discount_element.text.strip() if discount_element else None
        
        reviews_element = product.find('div', class_='rev')
        reviews = reviews_element.text.strip() if reviews_element else None
        
        
        data.append({'product name': product_name, 'price': price, 'discount': discount, 'reviews': reviews})

with open('jumia.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['product name', 'price', 'discount', 'reviews'])
    writer.writeheader()
    writer.writerows(data)
