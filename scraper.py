import requests
from bs4 import BeautifulSoup
from csv import writer

response = requests.get('https://webscraper.io/test-sites/e-commerce/allinone')

soup = BeautifulSoup(response.text, 'html.parser')

products = soup.find_all(class_='caption')

with open('posts.csv', 'w') as csv_file:
    csv_writer = writer(csv_file)
    headers = ['Title', 'Description', 'Price', 'Link']
    csv_writer.writerow(headers)

    for product in products:
        price = product.find(class_='pull-right price').get_text()
        title = product.find(class_='title').get_text()
        link = product.find('a')['href']
        description = product.find(class_='description').get_text()
        csv_writer.writerow([title, description, price, link])


