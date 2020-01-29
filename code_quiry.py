# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 13:01:54 2019

@author: CN261
"""
from requests.auth import HTTPBasicAuth
import requests
import json

with open(r'code_quiry.json','r') as readfile:
    code_quiry = json.load(readfile)

code_quiry['code_query_key']

url = 'https://codequiry.com/api/v1/account'

headers = {"Accept": "application/json",
           "apikey": code_quiry['code_query_key']}
response = requests.post(url,headers=headers)
response.text

""" Create check"""

data = {"name": "Test",
        "ID": "14",
        "language": "python"
        }
check_url = "https://codequiry.com/api/v1/check/create?name={}&language={}".format(data["name"],data["language"])
check_resp = requests.post(check_url,headers=headers)
output = check_resp.json()

# =============================================================================
# """ INsert the data into skillz database"""
# 
# code_quiry_lang = output['available_languages']
# code_quiry_lang_id = [code_quiry_lang[i]['id'] for i in range(len(code_quiry_lang))]
# code_quiry_languages = [code_quiry_lang[i]['language'].split(' (')[0] for i in range(len(code_quiry_lang))]
# 
# connection = mysql.connector.connect(host=database_auth['DB Host'], user=database_auth['DB Username'],port=3306,
#                passwd=database_auth['DB Password'], db=database_auth['Database'])
# cursor = connection.cursor()            
# import pandas as pd
# import numpy as np
# 
# code_quiry_df = pd.DataFrame(np.column_stack([code_quiry_lang_id,code_quiry_languages]),columns = ['code_quiry_lang_id','code_quiry_lang'])
# 
# 
# cursor.execute("""select * from sphere_engine_languages;""")
# skillz_languages_data = cursor.fetchall()
# 
# skillz_lang = [skillz_languages_data[i][1] for i in range(len(skillz_languages_data))]
# skillz_lang_first_name = [skillz_lang[i].split(' ')[0] for i in range(len(skillz_lang))]
# skillz_id = [skillz_languages_data[i][0] for i in range(len(skillz_languages_data))]
# skillz_df = pd.DataFrame(np.column_stack([skillz_id,skillz_lang]),columns = ['skillz_lang_id','skillz_lang'])
# 
# cqlid = []
# cqlang = []
# skzid = []
# sklang = []
# 
# for i in skillz_lang_first_name:
#     if i in code_quiry_df['code_quiry_lang'].values.tolist():
#         cqlid.append(code_quiry_df['code_quiry_lang_id'][code_quiry_df['code_quiry_lang'] == i].values.tolist())
#         cqlang.append(code_quiry_df['code_quiry_lang'][code_quiry_df['code_quiry_lang'] == i].values.tolist())    
#         skzid.append(skillz_df['skillz_lang_id'][skillz_df['skillz_lang'] == i].values.tolist())
#         sklang.append(skillz_df['skillz_lang'][skillz_df['skillz_lang'] == i].values.tolist())
# 
# cursor.execute("""show columns from code_quiry_languages;""")
# langs = cursor.fetchall()
# lang = [langs[i][0] for i in range(len(langs))]
# 
# master = pd.DataFrame(np.column_stack([cqlid,cqlang,skzid,sklang]),columns = lang)
# 
# code_quiry_id = [int(float(str(master['code_quiry_id'][i]))) for i in range(len(master))]
# skillz_lang_id = [int(float(str(master['code_quiry_id'][i]))) for i in range(len(master))]
# 
# 
# for i in range(len(master)):
#     sql_query = """Insert into code_quiry_languages (code_quiry_id,code_quiry_lang,skillz_lang_id,skillz_lang) values (%s,%s,%s,%s)"""
#     val = (code_quiry_id[i],master['code_quiry_lang'][i],
#            skillz_lang_id[i], master['skillz_lang'][i])
#     cursor.execute(sql_query,val)
#     connection.commit()
#     
# cursor.close()
# connection.close()
# 
# =============================================================================





