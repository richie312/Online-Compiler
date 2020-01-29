# -*- coding: utf-8 -*-


import json
import os
import webbrowser
os.chdir(r'D:\sphere_engine')

files = os.listdir(r'D:\sphere_engine')
with open('links.json','r') as readfile:
    links_dict = json.load(readfile)

# opent the links in chrome directly from the command line
#python3 -m webbrowser -t link_dict['sphere_api_documentation']
 
# Open url in a new window of the default browser, if possible
webbrowser.open_new(links_dict['sphere_api_documentation'])
 
# Open url in a new page (“tab”) of the default browser, if possible
webbrowser.open_new_tab(links_dict['sphere_handbook'])

dir(webbrowser)