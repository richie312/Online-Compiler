# -*- coding: utf-8 -*-
"""
Created on Fri Sep 20 09:13:27 2019

@author: CN261
"""

import requests
from sphere_engine.exceptions import SphereEngineException
from sphere_engine import ProblemsClientV4
from sphere_engine import CompilersClientV4
import webbrowser
problem_auth = {
        "endpoint" : "b47c8916.problems.sphere-engine.com",
        "token": "4c1e602f25ea827d81f3f84dbdbd9527"        
        }

# define access parameters
problem_accessToken = problem_auth["token"]
problem_endpoint = problem_auth["endpoint"]

client = ProblemsClientV4(problem_accessToken, problem_endpoint)

################################################################

""" get problem"""

data = {"level":"all"}

import requests
url = "http://127.0.0.1:5000/get_problems?level={}".format(data['level'])
#webbrowser.open_new_tab(url)
response = requests.get(url,data)
a = response.json()
a.keys()

""" OR """
url = "http://127.0.0.1:5000/get_problems?level=Easy"
resposne = requests.get(url)
response.json()

# create a problem

with open(r"problems\rotate_matrix.txt","r") as readfile:
    rotatematrix = readfile.read()

data = {
        "name": "Rotate Matrix",
        "body": rotatematrix,
        #"typeId": 0, #optional
        #"interactive": False, #optional
        "masterjudgeId": 1001,
        "level":"Difficult"
        }

url = 'http://127.0.0.1:5000/create_problem_id'
import requests
response = requests.post(url,json=data)
response.json()
    
""" create testcase"""
with open(r"testcases\rotatematrix\rotateMatrix_input.txt","r") as readfile:
    model_input = readfile.read()

with open(r"testcases\rotatematrix\rotateMatrix_output.txt","r") as readfile:
    model_output = readfile.read()

with open(r"testcases\rotatematrix\rotateMatrix_checkfile.py","r") as readfile:
    check_file = readfile.read()

data = {
        "id": 28972,
        "number": 1,
        "input_file": model_input,# optional
        "output_file": model_output, #optional
        "timelimit": 60,
        "judgeId": 1, 
        "active": False,
        "check_file": {"Python 3.x":check_file} # accepts dictionary lang:source for check_file
        }

#response = client.problems.getTestcase(28925,0)
#response
""" Testcase url"""
test_url = "http://127.0.0.1:5000/create_testcases"
result = requests.post(test_url,json = data)
result.json()

""" get problem_details"""
data = {"problemName": "Sort Words"}
url = 'http://127.0.0.1:5000/get_problem_details?problemName={}'.format(data['problemName'])
webbrowser.open_new_tab(url)
a = requests.get(url)
a.json()

""" create submissionId"""

with open(r"submissions\rotateMatrix_sub.py","r") as outfile:
    SourceFile = outfile.read()

submission_data = {
        "source": SourceFile,
        "language": "GA",
        "problem_name": "Rotate Matrix",
        "candidate_name": "Test123456"
        }


url = "http://111.93.164.108:5000/get_submissionId"

response = requests.post(url,json = submission_data)

response.json()

""" get result for the candidate"""
data = {"userName": "Prabhat",
        "problemName": "Rotate Matrix"
        }
url = "http://111.93.164.108:5000/get_result?userName={}&problemName={}".format(data['userName'],data['problemName'])
webbrowser.open_new_tab(url)
a = requests.get(url)
a.json()
client.submissions.get(2214827)
#############################################################################

""" update a problem"""

with open(r"problems/Dates of Easter.html","r") as readfile:
    body = readfile.read()
    
data = {
        "id": 29311,
        "name": "Dates of Easter",
        "masterjudgeId": 1001,
        "body": body, 
        "interactive": False
        }

url = "http://111.93.164.108:5000/update_problem"
import requests
a = requests.put(url,json = data)
a.json()

#client.submissions.create(27874, SourceFile, 116)
"""Update test case"""
with open(r"testcases\bubbleSort\bubbleSort_input.txt","r") as readfile:
    model_input = readfile.read()

with open(r"testcases\bubbleSort\bubbleSort_output.txt","r") as readfile:
    model_output = readfile.read()

with open(r"testcases\lexicographical\lexicographical_checkfile.js","r") as readfile:
    check_file = readfile.read()

data = {
        "id": 28955,
        "number": 0,
        #"input_file": model_input,# optional
        #"output_file": model_output, #optional
        "timelimit": 10,
        "judgeId": 1, 
        "active": True,
        "check_file": {"JavaScript [SpiderMonkey]":check_file} # accepts dictionary lang:source for check_file
        }
url = "http://111.93.164.108:5000/update_testcase"
import requests
result = requests.put(url,json = data)
result.text
result.json()

##########################

""" update checkfile recquired packages"""

url = "http://111.93.164.108:5000/update_checkfile_required_packages"
with open(r"testcases\easter_dates\requirement.go","r") as outfile:
    SourceFile = outfile.read()

data = {"language": "Go",
        "required_pckgs": SourceFile,
        "problem_id": 29311

        }

response = requests.put(url,json = data)
response.json()

"""Get Ranks"""

data = {"candidateName": "Ashutosh"}
url = "http://127.0.0.1:5000/get_ranking?candidateName={}".format(data['candidateName'])
import requests
result = requests.get(url,json = data)
result.json()

""" OR """

url = "http://127.0.0.1:5000/get_ranking"
import requests
result = requests.get(url)
result.json()


""" Get Test Cases"""

data = {"problemId": 28971,
        "language": "Go"}

import requests
url = "http://127.0.0.1:5000/get_testcases?problemId={}&language={}".format(data['problemId'],data['language'])
response = requests.get(url)
response.json()
""" OR """

response = requests.get('http://127.0.0.1:5000/get_testcases?problemId=28971&language=Python 3.x')
response.json()


""" Get Check File Required Packages"""

data = {"language": "Python",
        "problemId": str(28841)
        }
url = "http://111.93.164.108:5000/get_checkfile_required_packages?problemId={}&language=Go".format(data['problemId'])
response = requests.get(url)
response.json()

""" Delete Check File Required Packages"""

data = {"language": "",
        "problemId": 28841
        }
url = "http://111.93.164.108:5000/delete_checkfile_required_packages"
response = requests.delete(url,json = data)
response.json()


######################################################################