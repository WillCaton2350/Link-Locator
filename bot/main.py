from config.data import urls, nums
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import requests
import logging
import ssl

class parser:
    @staticmethod
    def get_subdomains():
        ssl._create_default_https_context = ssl.create_default_context
        try:
            with open('subdomains.csv', 'w') as file:
                for key, value in urls.url_dict.items(): 
                    try:
                        response = requests.get(value)
                        response.raise_for_status()  
                        soup = BeautifulSoup(response.content, 'html.parser')
                        for link in soup.find_all('a'):
                            file.writelines(link.get('href') + '\n'+ '\n')
                    except HTTPError as err:
                        logging.error(f"Failed to fetch URL: {value}, Error: {err}")
                        nums.retries += 1
        except Exception as e:
            logging.error(e)