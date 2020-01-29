# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 08:54:03 2019

@author: CN261
"""

import webbrowser
import json
from bs4 import BeautifulSoup
import requests
with open('links.json','r') as link_file:
    links = json.load(link_file)
    
questions = links['questions']    
webbrowser.open_new(questions)

""" take 5 easy questions """

first_reverse_url = "https://coderbyte.com/editor/First%20Reverse:Python"
webbrowser.open_new_tab(first_reverese_url)

# =============================================================================
# first_reverse_html = requests.get(first_reverse_url)
# soup = BeautifulSoup(first_reverse_html.content,'html.parser')
# text = soup.find_all('span')
# =============================================================================
