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

links.keys()    
questions = links['sphere_handbook']    
webbrowser.open_new(questions)
se_docs = links['sphere_api_documentation']
webbrowser.open_new(se_docs)


""" take 5 easy questions """
""" first Reverse"""
first_reverse_url = "https://coderbyte.com/editor/First%20Reverse:Python"
webbrowser.open_new_tab(first_reverse_url)

""" first factorial"""
first_factorial = "https://coderbyte.com/editor/First%20Factorial:Python"

""" Time Convert"""
time_convert = "https://coderbyte.com/editor/Time%20Convert:Python"

################## Medium Level Problem###################3333

"""Binary Gap"""

url = "https://app.codility.com/programmers/lessons/1-iterations/binary_gap/"
webbrowser.open_new_tab(url)

"""Sort Words (Lexicographical Order)"""

url = "https://www.geeksforgeeks.org/sort-words-lexicographical-order-python/"

""" Fibonnaci Sequence"""

url = "https://www.javatpoint.com/python-display-fibonacci-sequence-recursion##targetText=Python%20Program%20to%20Display%20Fibonacci%20Sequence%20Using%20Recursion&targetText=A%20Fibonacci%20sequence%20is%20a,13%20and%20so%20on..."

""" 

























