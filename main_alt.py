# -*- coding: utf-8 -*-

import flask
from flask import Flask, request, jsonify
from sphere_engine import ProblemsClientV4, CompilersClientV4
from sphere_engine.exceptions import SphereEngineException
from flask import render_template
import pandas as pd
import numpy as np
import time
import mysql.connector
import mysql
from datetime import datetime    
import json
import requests
import math
import webbrowser
from flask_cors import CORS, cross_origin


app = Flask(__name__,static_url_path='/static')
app.config['DEBUG'] = True
cors = CORS(app, resources={r"/*": {"origins": "*","headers":['Content-Type','Authorization','Origin','X-Requested-With','Accept'],"methods" :['GET','POST','PUT','PATCH','DELETE']}})
problem_auth = {
        'endpoint' : 'b47c8916.problems.sphere-engine.com',
        'token': '4c1e602f25ea827d81f3f84dbdbd9527'        
        }

# define access parameters
problem_accessToken = problem_auth['token']
problem_endpoint = problem_auth['endpoint']

client = ProblemsClientV4(problem_accessToken, problem_endpoint)

### Compiler API
compiler_auth = {
        "endpoint" : "b47c8916.compilers.sphere-engine.com",
        "token": "6fc402f585b35ef7accf61facc636af0"        
        }

# define access parameters
compiler_accessToken = compiler_auth["token"]
compiler_endpoint = compiler_auth["endpoint"]

compiler_client = CompilersClientV4(compiler_accessToken, compiler_endpoint)


# Problem API initialization
try:
    response_problem_api = client.test()
except SphereEngineException as e:
    if e.code == 401:
        print('Invalid access token')


# compiler Api initialization
        
try:
    compiler_response = compiler_client.test()
except SphereEngineException as e:
    if e.code == 401:
        print('Invalid access token')

###################################################################################################
###################################################################################################

''' Database config '''
with open('database_auth.json','r') as readfile:
    database_auth = json.load(readfile)

""" Server Call Back Functions"""


@app.route('/', methods=['GET'])
#@cross_origin(origin='*',headers=['Content-Type','Authorization','Origin','X-Requested-With','Accept'],methods = ['GET','POST','PUT','PATCH','DELETE'])
def home():
    return render_template('code_editor.html')

@app.route('/problem_widget', methods=['GET'])
#@cross_origin(origin='*',headers=['Content-Type','Authorization','Origin','X-Requested-With','Accept'],methods = ['GET','POST','PUT','PATCH','DELETE'])
def problem_widget():
    return render_template('problem_widget.html')

@app.route('/check_file_status', methods = ['GET'])
def check_file_status():

    return render_template('checkfile_status.html')

@app.route('/skillsz_api_docs', methods = ['GET'])
def skillsz_api_docs():

    return render_template('skillz_doc.html')




@app.route('/get_compiler_result', methods=['POST'])
def get_compiler_result():
    #data = request.args
    data = request.get_json()
    source = data["source"]
    language = data["language"]
    input_ = data["input"]
    connection = mysql.connector.connect(host=database_auth['DB Host'], user=database_auth['DB Username'],port=3306,
               passwd=database_auth['DB Password'], db=database_auth['Database'])
    cursor = connection.cursor()            
    cursor.execute("""select compilerID from skillz.sphere_engine_languages where language=%s;""",(language,))
    compilerId = cursor.fetchall()[0][0]
    try:
        compiler_response = compiler_client.submissions.create(source, compilerId,input_)
        time.sleep(5)
    
    except SphereEngineException as e:
        if e.code == 401:
            print('Invalid access token')
        elif e.code == 402:
            print('Unable to create submission')
        elif e.code == 400:
            print('Error code: ' + str(e.error_code) + ', details available in the message: ' + str(e))
    try:
        output = compiler_client.submissions.getStream(compiler_response['id'], 'output')
    except SphereEngineException as e:
        if e.code == 401:
            print('Invalid access token')
        elif e.code == 403:
            print('Access to the submission is forbidden')
        elif e.code == 404:
            print('Non existing resource, error code: ' + str(e.error_code) + ', details available in the message: ' + str(e))
        elif e.code == 400:
            print('Error code: ' + str(e.error_code) + ', details available in the message: ' + str(e))
        
    return jsonify({"Output" : output})
        

@app.route('/get_problems', methods=['GET'])
#@cross_origin(origin='*',headers=['Content-Type','Authorization','Origin','X-Requested-With','Accept'],methods = ['GET','POST','PUT','PATCH','DELETE'])
def get_problems():
    query_parameters = request.args
    level = query_parameters.get('level')
    connection = mysql.connector.connect(host=database_auth['DB Host'], user=database_auth['DB Username'],port=3306,
               passwd=database_auth['DB Password'], db=database_auth['Database'])
    cursor = connection.cursor()            
    try:
        if level == "all":
            cursor.execute("Select * from sphere_engine_problem_details;")
            data = cursor.fetchall()
            problem_id = [data[i][0] for i in range(len(data))]
            problem_code = [data[i][1] for i in range(len(data))]
            problem_name = [data[i][2] for i in range(len(data))]
            problem_description = [data[i][4] for i in range(len(data))]
            level = [data[i][5] for i in range(len(data))]
            response = {'problem_id': problem_id,
                        'problem_code': problem_code,
                        'problem_name': problem_name,
                        'problem_description': problem_description,
                        'level': level }
        else:
            
            cursor.execute("Select * from sphere_engine_problem_details where level=%s",(level,))
            data = cursor.fetchall()
            problem_id = [data[i][0] for i in range(len(data))]
            problem_code = [data[i][1] for i in range(len(data))]
            problem_name = [data[i][2] for i in range(len(data))]
            problem_description = [data[i][4] for i in range(len(data))]
            response = {'problem_id': problem_id,
                        'problem_code': problem_code,
                        'problem_name': problem_name,
                        'problem_description': problem_description}
    except NameError:
        print("Please enter the category of the problem; Easy/ Medium / Difficult or all")
    cursor.close()
    connection.close()
    return (json.dumps(response))
    
@app.route('/get_submissionId',methods=['POST'])
#@cross_origin(origin='*',headers=['Content-Type','Authorization','Origin','X-Requested-With','Accept'],methods = ['GET','POST','PUT','PATCH','DELETE'])
def submission_id():
    #client = ProblemsClientV4(problem_accessToken, problem_endpoint)
    submission_data = request.get_json()
    source = submission_data['source']
    lang = submission_data['language']
    problem_name = submission_data['problem_name']
    candidate_name = submission_data['candidate_name']
    connection = mysql.connector.connect(host=database_auth['DB Host'], user=database_auth['DB Username'],port=3306,
               passwd=database_auth['DB Password'], db=database_auth['Database'])
    cursor = connection.cursor()
    cursor.execute("""select compilerID from sphere_engine_languages where language=%s""",(lang,))
    compilerID = cursor.fetchall()[0][0]
    cursor.execute("""select id from sphere_engine_problem_details where name = %s;""", (problem_name,))
    problem_id = cursor.fetchone()[0]
    """ get the checker file specfic to the compiler and the problemId"""
    cursor.execute("""select check_file from sphere_engine_testcase where problem_id=%s;""", (problem_id,))
    check_file_all = eval(cursor.fetchall()[0][0])
    check_file = check_file_all[lang]
    """ Send the file to the compiler"""
    submission_file = source + check_file
    """ Submission file """
    try:
        response = client.submissions.create(problem_id, submission_file, compilerID)
    except SphereEngineException as e:
        if e.code == 401:
            response = 'Invalid access token'
        elif e.code == 402:
            response = 'Unable to create submission'
        elif e.code == 400:
            response = 'Error code: ' + str(e.error_code) + ', details available in the message: ' + str(e)

    """ Database Insertion of Submission Ids"""
    sql_query = """INSERT INTO sphere_engine_submissionid (id,language,sourcefile,problemId,candidatename) VALUES(%s, %s,%s,%s,%s);"""
    val = (response['id'],lang,source,problem_id,candidate_name)
    cursor.execute(sql_query,val)
    connection.commit()
    connection.close()
    # Close the connection after the successful insertion
    cursor.close()
    return jsonify({"submissionId": response['id']})

@app.route('/get_problem_details',methods = ['GET'])
#@cross_origin(origin='*',headers=['Content-Type','Authorization','Origin','X-Requested-With','Accept'],methods = ['GET','POST','PUT','PATCH','DELETE'])
def problem_details():
    """ get the system arguments"""
    query_parameters = request.args
    problem_name = query_parameters.get('problemName')
    connection = mysql.connector.connect(host=database_auth['DB Host'], user=database_auth['DB Username'],port=3306,
               passwd=database_auth['DB Password'], db=database_auth['Database'])
    cursor = connection.cursor()            
    try:
        sql_query = "select * from sphere_engine_problem_details where name=%s"
        cursor.execute(sql_query,(problem_name,))
        result = cursor.fetchone()    
        response1 = [result[i] for i in range(len(result))] 
        # change the date to string
        response1[11] = response1[11].isoformat()
        sql_query = "show columns from sphere_engine_problem_details;"
        cursor.execute(sql_query)
        columns = cursor.fetchall()
        cursor.close()
        a = [columns[i][0] for i in range(len(columns))]
        # make the dictionary 
        response = {}
        for i in range(len(response1)):
            response[a[i]] = response1[i]

    except TypeError: 
        response = "<h3 style=color:red;font-family:verdana;>{} problem not found in the database. Please either create a new problem or enter a valid problem.</h3>".format(problem_name)
    
    if type(response) != dict or type(response) == str:
        return response
    else:
        return jsonify(response)

@app.route('/get_result',methods=['GET'])
#@cross_origin(origin='*',headers=['Content-Type','Authorization','Origin','X-Requested-With','Accept'],methods = ['GET','POST','PUT','PATCH','DELETE'])
def get_result():
    client = ProblemsClientV4(problem_accessToken, problem_endpoint)
    connection = mysql.connector.connect(host=database_auth['DB Host'], user=database_auth['DB Username'],port=3306,
               passwd=database_auth['DB Password'], db=database_auth['Database'])
    cursor = connection.cursor()            
    query_parameters = request.args
    candidatename = query_parameters.get('userName')
    problem_name = query_parameters.get('problemName')
    cursor.execute("""select id from sphere_engine_problem_details where name=%s; """,(problem_name,))
    problem_id = cursor.fetchall()[0][0]
    cursor.execute("""select id from sphere_engine_submissionid where candidatename=%s and problemId=%s; """,(candidatename,problem_id,))
    submission = cursor.fetchall()    
    # Instantiate dict to store the values from the json
    result = {}
    string_id  =[str(submission[i][0]) for i in range(len(submission))]
    for i in range(len(submission)):
        try:
            response = client.submissions.get(int(submission[i][0]))
            result[string_id[i]] = response
        except SphereEngineException as e:
            if e.code == 401:
                result = 'Invalid access token'
            elif e.code == 403:
                result = 'Access to the submission is forbidden'
            elif e.code == 404:
                result = 'Submission does not exist'
    # Store the data if and only if the Submission id is not in databse
    time.sleep(5.0)
    ids = [submission[i][0] for i in range(len(submission))]
    # match submission id with result table in databse
    cursor.execute("""select submissionid from result_sphere_engine where candidateName=%s and problem_name=%s""",(candidatename,problem_name,))
    result_db_ids = cursor.fetchall()
    result_db_ids = [result_db_ids[i][0] for i in range(len(result_db_ids))]
    for ID in ids:
        if ID in result_db_ids:
            None
        else:        
            """ Result Insertion into DB"""
            cursor = connection.cursor()
            sql_query = """show columns from result_sphere_engine;"""
            cursor.execute(sql_query)
            column_keys = cursor.fetchall()
            columns = [column_keys[i][0] for i in range(len(column_keys)-1)] 
            list_result_keys = list(result.keys())
            place_holder = ['%s' for i in range(len(columns))]
            for i in range(len(list_result_keys)):
                sql_query = """INSERT INTO result_sphere_engine ({}) VALUES({});""".format(",".join(columns),",".join(place_holder))
                val = (list_result_keys[i],result[list_result_keys[i]]['compiler']['id'],
                       result[list_result_keys[i]]['compiler']['version']['name'],
                       result[list_result_keys[i]]['executing'],
                       result[list_result_keys[i]]['problem']['code'],result[list_result_keys[i]]['problem']['id'],
                       result[list_result_keys[i]]['problem']['name'],json.dumps(result[list_result_keys[i]]['result']),
                       result[list_result_keys[i]]['result']['status']['name'],candidatename)
                cursor.execute(sql_query,val)
                connection.commit()
                
    connection.close()
    return jsonify(result)

""" Create Problem"""    
@app.route('/create_problem_id',methods=['POST'])
#@cross_origin(origin='*',headers=['Content-Type','Authorization','Origin','X-Requested-With','Accept'],methods = ['GET','POST','PUT','PATCH','DELETE'])
def create_problem():
    """ Input data contains the key value pair, which is passed to the api in order
    to create the problemID"""
    client = ProblemsClientV4(problem_accessToken, problem_endpoint)
    data = request.get_json()
    output = client.problems.create(data['name'],masterjudge_id = 1001,body=data['body'])
    time.sleep(0.5)
    connection = mysql.connector.connect(host=database_auth['DB Host'], user=database_auth['DB Username'],port=3306,
           passwd=database_auth['DB Password'], db=database_auth['Database'])
    cursor = connection.cursor()            
    Created_Date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    level = data['level']    
    response = client.problems.get(output['id'])
    val = (response['id'],response['code'],response['name'],response['shortBody'],response['body'],
            json.dumps(response['type']),response['interactive'],json.dumps(response['masterjudge']['id']),
            json.dumps(response['testcases']),json.dumps(response['lastModified']),json.dumps(response['permissions']),Created_Date,level)
    sql_query = "INSERT INTO sphere_engine_problem_details (id,code,name,shortBody,body,type,interactive,masterjudge,testcases,lastModified, permissions,Created_Date,level) VALUES (%s, %s, %s, %s, %s, %s, %s,%s,%s,%s,%s,%s,%s)"     
    cursor.execute(sql_query,val)
    connection.commit()
    connection.close()
    return jsonify(output)

@app.route('/create_testcases',methods=['POST'])
#@cross_origin(origin='*',headers=['Content-Type','Authorization','Origin','X-Requested-With','Accept'],methods = ['GET','POST','PUT','PATCH','DELETE'])
def create_testcases():
    client = ProblemsClientV4(problem_accessToken, problem_endpoint)
    test_data = request.get_json()
    response = client.problems.createTestcase(test_data['id'], test_data['input_file'], test_data['output_file'], test_data['timelimit'], test_data['judgeId'])
    time.sleep(0.5)
    """ Submission of test cases into the database """
    connection = mysql.connector.connect(host=database_auth['DB Host'], user=database_auth['DB Username'],port=3306,
                               passwd=database_auth['DB Password'], db=database_auth['Database'])
    cursor = connection.cursor()
    cursor.execute("""select problem_id from sphere_engine_testcase;""")
    list_probids = cursor.fetchall()
    problemids = [str(list_probids[i][0]) for i in range(len(list_probids))]
    lang = list(test_data['check_file'].keys())[0]
    if str(test_data['id']) not in problemids:
        sql_query = """INSERT INTO sphere_engine_testcase (number,problem_id,input_file,output_file,created_date,timelimit,judgeId,check_file) VALUES (%s,%s,%s,%s,%s,%s,%s,%s);"""
        val  = (response['number'],test_data['id'],test_data['input_file'], test_data['output_file'],datetime.now().strftime('%Y-%m-%d'),test_data['timelimit'], test_data['judgeId'],json.dumps(test_data['check_file']))
        cursor.execute(sql_query,val)
        connection.commit()
    else:
        cursor.execute("SET SQL_SAFE_UPDATES=0")
        connection.commit()
        """ get the available check_file dictionary from the database"""
        cursor.execute("""Select check_file from sphere_engine_testcase where problem_id = {}""".format(test_data['id']))
        check_file_dictionary = eval(cursor.fetchall()[0][0])
        if lang in check_file_dictionary:
            check_file_dictionary[lang] = test_data['check_file'][lang]
        else :
            check_file_dictionary[lang] = test_data['check_file'][lang]
        sql_query = """INSERT INTO sphere_engine_testcase (number,problem_id,input_file,output_file,created_date,timelimit,judgeId,check_file) VALUES (%s,%s,%s,%s,%s,%s,%s,%s);"""
        val  = (response['number'],test_data['id'],test_data['input_file'], test_data['output_file'],datetime.now().strftime('%Y-%m-%d'),test_data['timelimit'], test_data['judgeId'],str(json.dumps(check_file_dictionary)))
        cursor.execute(sql_query,val)
        connection.commit()
    cursor.close()
    connection.close()
    metadata = response
    metadata.update(test_data)
    return jsonify(metadata)

@app.route('/update_problem',methods=['PUT'])
#@cross_origin(origin='*',headers=['Content-Type','Authorization','Origin','X-Requested-With','Accept'],methods = ['GET','POST','PUT','PATCH','DELETE'])
def update_problem():
    client = ProblemsClientV4(problem_accessToken, problem_endpoint)
    data = request.get_json()
    response = client.problems.update(data['id'],data['name'],1001,data['body'],data['interactive'])
    # update the same in local database.
    connection = mysql.connector.connect(host=database_auth['DB Host'], user=database_auth['DB Username'],port=3306,
                               passwd=database_auth['DB Password'], db=database_auth['Database'])
    cursor = connection.cursor()
    cursor.execute("SET SQL_SAFE_UPDATES=0")
    connection.commit()
    
    response = client.problems.get(data['id'])
    list_sphere_keys= list(response.keys())
    values  = (response['id'],response['code'],response['name'],response['shortBody'],response['body'],
            json.dumps(response['type']),response['interactive'],json.dumps(response['masterjudge']['id']),
            json.dumps(response['testcases']),json.dumps(response['lastModified']),json.dumps(response['permissions']))
    
    """ update the fields in the database on the basis of incoming data from sphere engine"""     
    for i in range(len(list_sphere_keys)):
        cursor.execute("""UPDATE sphere_engine_problem_details SET {}=%s where id=%s;""".format(list_sphere_keys[i]),(values[i],data['id'],))
        connection.commit()
    cursor.close()
    connection.close()
    return jsonify({"Data Updated in the database":"True",'newproblemName':response['name']})


@app.route('/update_testcase',methods=['PUT'])
#@cross_origin(origin='*',headers=['Content-Type','Authorization','Origin','X-Requested-With','Accept'],methods = ['GET','POST','PUT','PATCH','DELETE'])
def update_testcase():
    client = ProblemsClientV4(problem_accessToken, problem_endpoint)
    data = request.get_json()
    key_list = list(data.keys())
    list_all_params = ['id', 'number', 'input_file', 'output_file', 'timelimit', 'judgeId', 'active', 'check_file']
    diff_list = list(set(list_all_params) - set(key_list))
    """ Assign each element in diff_list as None"""
    val = {}
    for i in range(len(data)):
        val[key_list[i]] = data[key_list[i]]
        
    optional_params = {}
    for i in range(len(diff_list)):
        optional_params[diff_list[i]] = None
    
    val.update(optional_params)
    
    response = client.problems.updateTestcase(val['id'],val['number'],val['input_file'],val['output_file'],
                                              val['timelimit'],val['judgeId'],val['active'])
    # update the same in local database.
    connection = mysql.connector.connect(host=database_auth['DB Host'], user=database_auth['DB Username'],port=3306,
                               passwd=database_auth['DB Password'], db=database_auth['Database'])
    cursor = connection.cursor()
    cursor.execute('set innodb_lock_wait_timeout=10000')
    connection.commit()
    cursor.execute("SET SQL_SAFE_UPDATES=0")
    connection.commit()
    """ get the latest updated testcases of the problemId"""
    url = "https://{}/api/v4/problems/{}/testcases?access_token={}".format(problem_auth['endpoint'],data['id'],problem_auth['token'])
    testcases = requests.get(url).json()
    numbers = [testcases['items'][i]['number'] for i in range(len(testcases['items']))]
    active = [testcases['items'][i]['active'] for i in range(len(testcases['items']))]
    judge_id = [testcases['items'][i]['judge'] for i in range(len(testcases['items']))]
    testcase_dict = {'number': numbers,
                     'active': active,
                     'judge_id': judge_id}
    key_list_excl_id = key_list[1:]

    ## check if the check file is passed or not?
    if 'check_file' in key_list_excl_id:
        #data['check_file'] =json.dumps(data['check_file'])
        cursor.execute("""select check_file from sphere_engine_testcase where problem_id= {}""".format((data['id'])))
        check_file_dict = eval(cursor.fetchall()[0][0])
        check_file_dict.update(data['check_file'])
        cursor.execute("""update sphere_engine_testcase set check_file=%s where problem_id=%s""",(json.dumps(check_file_dict),data['id']))
        connection.commit()
        cursor.execute("""update sphere_engine_testcase SET test_case_dict=%s where problem_id=%s""",(str(json.dumps(testcase_dict)),data['id']))
        connection.commit()
        
    else:
        for i in range(len(key_list_excl_id)):
            if key_list_excl_id[i] in ['number','active']: 
                   cursor.execute("""update sphere_engine_testcase set test_case_dict=%s where problem_id=%s""",(str(json.dumps(testcase_dict)),data['id']))
                   connection.commit()
            else:    
                cursor.execute("""update sphere_engine_testcase set {}=%s where problem_id=%s""".format(key_list_excl_id[i]),(data[key_list_excl_id[i]],data['id']))
                connection.commit()
         
    connection.close()
    cursor.close()
    return jsonify({'Updated':True})

@app.route('/get_ranking',methods=['GET'])
#@cross_origin(origin='*',headers=['Content-Type','Authorization','Origin','X-Requested-With','Accept'],methods = ['GET','POST','PUT','PATCH','DELETE'])
def get_ranking():
    connection = mysql.connector.connect(host=database_auth['DB Host'], user=database_auth['DB Username'],port=3306,
               passwd=database_auth['DB Password'], db=database_auth['Database'])
    cursor = connection.cursor()                
    query_parameters = request.args
    candidateName = query_parameters.get('candidateName')    
        
    if candidateName is not None:
        cursor.execute("Select submissionID from result_sphere_engine where candidateName=%s",(candidateName,))
        sub_data = cursor.fetchall()
        sub_id = [sub_data[i][0] for i in range(len(sub_data))]
        data = []
        for i in range(len(sub_id)):    
            cursor.execute("Select ranking from result_sphere_engine where submissionId=%s",(sub_id[i],))
            ranks = cursor.fetchall()
            data.append(ranks[0][0])    
        response = {"name":candidateName,
                    "Rank": data}         
        
    else:
        cursor.execute("Select result, status, candidateName,submissionId from result_sphere_engine;")
        data = cursor.fetchall()
        result = [json.loads(data[i][0]) for i in range(len(data))]
        status = [data[i][1] for i in range(len(data))]
        name = [data[i][2] for i in range(len(data))]    
        submissionId = [data[i][3] for i in range(len(data))]
        score = [result[i]['score'] for i in range(len(data))]
        time = [result[i]['time'] for i in range(len(data))]
        number_of_cases = []
        for i in range(len(data)):
            try:    
                number_of_cases.append(len(result[i]['testcases']))
            except TypeError:
                number_of_cases.append(1)
        
        """ get the weighted score"""
        weighted_score = []
        for i in range(len(data)):
            if score[i] == 0:
                weighted_score.append(0)
            else:
                try:
                    weighted_score.append(0.70*score[i] + 0.20*number_of_cases[i])
                except TypeError:
                    None
                    
        df = pd.DataFrame(np.column_stack([name,submissionId,status,score,weighted_score]),columns = ['name','SubmissionID','status','score','weighted_score'])
        df = df.sort_values('weighted_score',ascending = False)
        df = df.reset_index(drop = True)    
        
        """ get the ranking """
        ranking = []
        for i in range(len(df)):
            if int(float(df['score'][i])) == 0:
               ranking.append('Not Applicable due to {}'.format(df['status'][i])) 
            else:
                ranking.append(i+1)
            
        rank_df = pd.DataFrame(np.column_stack([df['name'].values.tolist(),df['SubmissionID'].values.tolist(),ranking]),columns = ['name','SubmissionId','rank'])        
        """ Database Insertion"""
        for i in range(len(rank_df)):
            cursor.execute("SET SQL_SAFE_UPDATES=0")
            connection.commit()
            cursor.execute("Update result_sphere_engine set ranking=%s where submissionID=%s",(rank_df['rank'][i],rank_df['SubmissionId'][i]))
            connection.commit()            
        cursor.close()
        connection.close()
        response = {"Candidate Name": rank_df['name'].values.tolist(),
                    "SubmissionId":rank_df['SubmissionId'].values.tolist(),
                    "Rank": rank_df['rank'].values.tolist()}        
        
    return jsonify(response)

@app.route('/get_testcases',methods=['GET'])
def get_testcases():
    connection = mysql.connector.connect(host=database_auth['DB Host'], user=database_auth['DB Username'],port=3306,
               passwd=database_auth['DB Password'], db=database_auth['Database'])
    cursor = connection.cursor()                
    query_parameters = request.args
    problemId = query_parameters.get('problemId')
    language = query_parameters.get('language')
    cursor.execute("select compilerID from sphere_engine_languages where language=%s",(language,))
    compiler = cursor.fetchall()[0][0]
    cursor.execute("select check_file,test_case_dict from sphere_engine_testcase where problem_id=%s",(problemId,))
    data = cursor.fetchall()
    check_file = eval(data[0][0])
    testcase_details = data[0][1]
    return jsonify({"check_file": check_file[language],
                    "testcases": testcase_details})

if __name__ == '__main__':
    app.run(host = '0.0.0.0',port = 5000,debug = True)
