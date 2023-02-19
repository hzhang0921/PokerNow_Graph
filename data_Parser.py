import pandas as pd
import os
from csv import DictReader
import pprint

def csv_to_dict(file_name):
    os.chdir("/Users/haoyang/Documents/VScode/Python/PokerNow_Graph/Graph_CSV_Files")
    # cwd = os.getcwd()  # Get the current working directory (cwd)
    # files = os.listdir(cwd)  # Get all the files in that directory
    # df = pd.read_csv("Sample_Ledger.csv").to_string().split()
    
    csv_name = file_name
    with open(csv_name, 'r') as data:
        dict_reader = DictReader(data)
        list_of_dict = list(dict_reader)
    return list_of_dict

def Data_to_list(list_of_dict):
    #Convert list of dicts into one lined list
    list_logs = []
    for dicts in list_of_dict:
            list_logs.insert(0, dicts['entry']) #\ufeffentry sometimes

    final_logs = [[]] 
    count = 0
    for logs in list_logs: 
        if 'ending hand' in logs:
            count += 1
            final_logs.append([])
        else:   
             final_logs[count].append(logs)
             
    final_list = []
    count = 0
    for lists in final_logs:
         for lines in lists:
              if 'Player stacks:' in lines:
                    count += 1
                    temp_list = lines[15:]
                    values = temp_list.split('|')
                    temp_dict = {}
                    for value in values:
                        users = value.split("\"")
                        temp_dict[users[1]] = float(users[2].replace("(","").replace(")","").replace(" ",""))
                    final_list.append(temp_dict)
    
    return final_list

def collect_names(list_of_dict):
    name_list = []
    for dictionaries in list_of_dict:
        for keys in dictionaries.keys():
            if keys not in name_list:
                 name_list.append(keys)
    return name_list

def data_to_points(key_name, list_of_dict):
    yvalues = []
    for dictionaries in list_of_dict:
        if key_name in dictionaries:
            yvalues.append(dictionaries[key_name])
        else:
            yvalues.append(0)
    return yvalues

def main_run(file_name):
    converted_data = csv_to_dict(file_name)
    Data = Data_to_list(converted_data)
    print(collect_names(Data))
    return Data



