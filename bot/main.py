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
                for i in range(nums.num_executions):
                    with open(f'subdomains{i}.csv', 'w') as file:
                        for url in urls.url_list: 
                            try:
                                value = urls.url_list[i]
                                response = requests.get(value)
                                response.raise_for_status()
                                soup = BeautifulSoup(response.content, 'html.parser')
                                for link in soup.find_all('a'):
                                    file.writelines(link.get('href') + '\n'+ '\n')
                            except HTTPError as err:
                                logging.error(f"Failed to fetch URL: {url}, Error: {err}")
            except Exception as err:
                logging.error(err)