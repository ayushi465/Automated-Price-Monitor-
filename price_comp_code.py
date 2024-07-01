import json
import logging
import requests
from bs4 import BeautifulSoup
from time import sleep
import schedule
import smtplib
import os
import time

# Setting up logging
logging.basicConfig(level=logging.INFO, filename='price_comparison.log', filemode='a', format='%(asctime)s - %(levelname)s - %(message)s')
logging.info("Script started.")

# Load configuration
with open('config.json') as config_file:
    config = json.load(config_file)

logging.info("Configuration loaded.")

# Email configuration
recipient = config['email']['recipient']
sender = config['email']['sender']
password = config['email']['password']

def send_email(subject, body):
    try:
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(sender, password)
        
        headers = "\r\n".join([
            "from: " + sender,
            "subject: " + subject,
            "to: " + recipient,
            "mime-version: 1.0",
            "content-type: text/html"
        ])
        content = headers + "\r\n\r\n" + body
        s.sendmail(sender, recipient, content)
        s.quit()
        logging.info(f"Email sent: {subject}")
    except Exception as e:
        logging.error(f"Error sending email: {e}")

def fetch_amazon_price(search_url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'}
    try:
        logging.info(f"Fetching Amazon URL: {search_url}")
        start_time = time.time()
        response = requests.get(search_url, headers=headers)
        elapsed_time = time.time() - start_time
        logging.info(f"Fetched URL in {elapsed_time:.2f} seconds.")
        sleep(1)

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'lxml')
            price = None
            price_tag = soup.find('span', {'class': 'a-price-whole'})
            if price_tag:
                price = price_tag.text.strip().replace(',', '')
                price = float(price)
            return price
        else:
            logging.error(f"Failed to fetch {search_url}: Status code {response.status_code}")
            return None
    except Exception as e:
        logging.error(f"Error fetching price from {search_url}: {e}")
        return None

def fetch_flipkart_price(search_url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36'}
    try:
        logging.info(f"Fetching Flipkart URL: {search_url}")
        start_time = time.time()
        response = requests.get(search_url, headers=headers)
        elapsed_time = time.time() - start_time
        logging.info(f"Fetched URL in {elapsed_time:.2f} seconds.")
        sleep(1)

        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'lxml')
            price = None
            price_tag = soup.find('div', {'class': '_30jeq3 _16Jk6d'})
            if price_tag:
                price = price_tag.text.strip().replace('₹', '').replace(',', '')
                price = float(price)
            return price
        else:
            logging.error(f"Failed to fetch {search_url}: Status code {response.status_code}")
            return None
    except Exception as e:
        logging.error(f"Error fetching price from {search_url}: {e}")
        return None

def check_product_prices(product):
    product_name = product['name']
    amazon_search_url = product['amazon_search_url']
    flipkart_search_url = product['flipkart_search_url']
    prices = []

    amazon_price = fetch_amazon_price(amazon_search_url)
    if amazon_price:
        prices.append(("Amazon", amazon_price, amazon_search_url))

    flipkart_price = fetch_flipkart_price(flipkart_search_url)
    if flipkart_price:
        prices.append(("Flipkart", flipkart_price, flipkart_search_url))

    if prices:
        prices.sort(key=lambda x: x[1])  # Sort by price
        best_source, best_price, best_url = prices[0]
        logging.info(f"Best price for {product_name} is ₹{best_price} on {best_source} ({best_url})")

        # Send email notification
        subject = f'{product_name} Price Alert'
        body = f'The best price for {product_name} is now ₹{best_price} on {best_source}. Check it out here: {best_url}'
        send_email(subject, body)
    else:
        logging.info(f"No valid prices found for {product_name}")

def job():
    logging.info("Starting scheduled job...")
    products = config['products']
    logging.info(f"Total products to check: {len(products)}")
    for i, product in enumerate(products):
        logging.info(f"Checking product {i + 1}/{len(products)}: {product['name']}")
        check_product_prices(product)

# Schedule the job
schedule.every(1).hour.do(job)

while True:
    schedule.run_pending()
    sleep(1)
