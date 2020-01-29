# -*- coding: utf-8 -*-
"""
Created on Wed Nov  6 14:38:37 2019

@author: CN261
"""

compiler_auth = {
        "endpoint" : "b47c8916.compilers.sphere-engine.com",
        "token": "6fc402f585b35ef7accf61facc636af0"        
        }

# define access parameters
compiler_accessToken = compiler_auth["token"]
compiler_endpoint = compiler_auth["endpoint"]

compiler_client = CompilersClientV4(compiler_accessToken, compiler_endpoint)

# API usage
try:
    response = compiler_client.test()
except SphereEngineException as e:
    if e.code == 401:
        print('Invalid access token')

"""Compiler Data"""
with open("source.py","r") as readfile:
    source = readfile.read()

data = {
        "source": source,
        "language" : "Python 3.x",
        "input" : 10
        }

source = data['source']
compilerId = 116
input = data['input']


try:
    response = compiler_client.submissions.create(source, compilerId, input)
    # response['id'] stores the ID of the created submission
except SphereEngineException as e:
    if e.code == 401:
        print('Invalid access token')
    elif e.code == 402:
        print('Unable to create submission')
    elif e.code == 400:
        print('Error code: ' + str(e.error_code) + ', details available in the message: ' + str(e))

response['id']


try:
    response = compiler_client.submissions.get(response['id'])
except SphereEngineException as e:
    if e.code == 401:
        print('Invalid access token')
    elif e.code == 403:
        print('Access to the submission is forbidden')
    elif e.code == 404:
        print('Submission does not exist')

""" get the compiler_sub details"""

try:
    output = compiler_client.submissions.getStream(response['id'],'output')
except SphereEngineException as e:
    if e.code == 401:
        print('Invalid access token')
    elif e.code == 403:
        print('Access to the submission is forbidden')
    elif e.code == 404:
        print('Submission does not exist')

compiler_client.submissions.getStream(88024376, 'output')
import requests

with open("source.py","r") as readfile:
    source = readfile.read()

data = {
        "source": source,
        "language" : "Python 3.x",
        "input" : 5
        }
    
url_sub = "https://b47c8916.compilers.sphere-engine.com/api/v4/submissions?access_token=6fc402f585b35ef7accf61facc636af0"
requests.post(url_sub,data = data)
request.json()

url = "http://111.93.164.108:5000/get_compiler_result"
#local_url = "http://127.0.0.1:5000/get_compiler_result"
result = requests.post(url,json = data)
result.json()


url = "https://b47c8916.compilers.sphere-engine.com/api/v4/submissions/{}/output?access_token=6fc402f585b35ef7accf61facc636af0".format(88111059)

a = requests.get(url)
a.json()
