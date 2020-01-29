# -*- coding: utf-8 -*-

import re
import pandas as pd
import numpy as np    

def dataframe_plot(logfile):
    import re
    import pandas as pd
    import numpy as np    
    
    api_status = []
    for i in range(len(logfile)):
        pattern = r"^\d{1,200}\.\d{1,200}\.\d{1,200}\.\d{1,200}"
        try:
            a = re.search(pattern,logfile[i])
            api_status.append(a.string)
        except AttributeError:
            None
    
    """ get the dates and the code"""        
    ip_date=[api_status[i].split("\"")[0].split('[')[1][:-2] if api_status[i].split("\"")[0] !="" else "None" for i in range(len(api_status))] 
    
    strcode = []
    for i in range(len(api_status)):
        try:
            try:
                dig_pat = r'^ \d{1,9}\d{0,9}\d{0,9}\ '
                b = re.search(dig_pat,api_status[i].split("\"")[2])
                strcode.append(b.string[1:-3])
            except AttributeError:
                strcode.append("NA")
        except IndexError:
            strcode.append("NA")
    
    """ convert to integers"""
    code = []
    
    for i in range(len(strcode)):
        try:
            code.append(int(strcode[i]))
        except ValueError:
            code.append(0)
    
    
    """ get the api"""
    api_type = []
    rawapi = []
    for i in range(len(api_status)):
        try:
            api_type.append(api_status[i].split("\"")[1].split('/')[0][:-1])
            rawapi.append(api_status[i].split("\"")[1].split('/')[1].split(' ')[0])
        except IndexError:
            api_type.append("NA")
            rawapi.append("NA")
    
    with open(r'list_api.txt','r') as readfile:
        api_list = readfile.readlines()      
    
    api_list = [api_list[i][:-1] for i in range(len(api_list))]
    
    for i in range(len(rawapi)):
        if rawapi[i] in api_list:
            rawapi[i] = api_list[api_list.index(rawapi[i])]
        elif rawapi[i].split('?')[0] in api_list:
            rawapi[i]= api_list[api_list.index(rawapi[i].split('?')[0])]
        else:
            rawapi[i] = "None"
    
    df = pd.DataFrame(np.column_stack([ip_date,rawapi,code]),columns = ["Date","API","Code"])
    
    for i in range(len(df)):
        try:
            df['Date'][i] = pd.to_datetime(df['Date'][i])
        except ValueError:
            df['Date'][i] = "Not Available"

    """ get additional month column wrt dates"""
    Month = []
    
    for i in range(len(df)):
        try:
            Month.append(df['Date'][i].month)
        except AttributeError:
            Month.append(0)
            
    """add the month column in df"""
    df['Month'] = Month
    df['Code'][df['API'] == 'None'] = 0
    df['Code'] = df['Code'].astype(int)
    df = df.drop(['Date'],axis =1)
    """ Analytics of API Performance"""
    """ Filter by Error Category"""
    success_df = df[(df['Code'] >= 200) & (df['Code'] < 300)]
    Redirects_df = df[(df['Code'] >= 300) & (df['Code'] < 400)]
    Client_Errors_df = df[(df['Code'] >= 400) & (df['Code'] < 500)]
    Server_errors_df = df[df['Code'] >= 500]
    
    """ get the count of each api for error category"""
    
    success = success_df.groupby(['Month','API','Code'])
    success_df = pd.DataFrame(success.size().reset_index(name = "Group_Count"))
    redirects = Redirects_df.groupby(['Month','API','Code'])
    redirect_df = pd.DataFrame(redirects.size().reset_index(name = "Group_Count"))
    Client_Errors = Client_Errors_df.groupby(['Month','API','Code'])
    clerror_df = pd.DataFrame(Client_Errors.size().reset_index(name = "Group_Count"))
    server_error = Server_errors_df.groupby(['Month','API','Code'])
    servererr_df = pd.DataFrame(server_error.size().reset_index(name = "Group_Count"))

    return {"success":success_df,"redirects":redirect_df,"Client_Error":clerror_df,"Server_Error":servererr_df}


    
