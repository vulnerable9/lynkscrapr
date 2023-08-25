#!/usr/bin/python3

from bs4 import BeautifulSoup
import requests
from colorama import *

print("Lynkscrapr - scrape weblinks with ease.")

url = input(Fore.CYAN+"Enter a URL with http/https - "+Fore.RESET)
response = requests.get(url)
html_content = response.content

soup = BeautifulSoup(html_content, 'html.parser')

links = soup.find_all('a')
for link in links:
    print(Fore.GREEN+link.get('href')+Fore.RESET)

input("Press Enter To Exit")