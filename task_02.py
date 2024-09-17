import requests
from bs4 import BeautifulSoup
import csv
URL = "http://books.toscrape.com/" 
response = requests.get(URL)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    
    with open('books_data.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Title', 'Price', 'Availability', 'Rating'])
        books = soup.find_all('article', class_='product_pod')
        
        for book in books:
            # Get the title,price,avaliability amd rating of books of the book
            title = book.h3.a['title']
            price = book.find('p', class_='price_color').text.strip()
            availability = book.find('p', class_='instock availability').text.strip()
            rating_tag = book.find('p', class_='star-rating')
            rating = rating_tag['class'][1] if rating_tag else 'No Rating'
            writer.writerow([title, price, availability, rating])

    print("Data has been successfully scraped and saved to 'books_data.csv'")
else:
    print(f"Failed to retrieve the website. Status code: {response.status_code}")

                 