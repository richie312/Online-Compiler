# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 11:22:16 2019

@author: CN261
"""

client = ProblemsClientV4(problem_accessToken, problem_endpoint)
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