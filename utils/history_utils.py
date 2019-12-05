from chess import *
import json
import os


def write_history_table(history_table):
    table_json = json.dumps(history_table)
    f = open(os.getcwd()+"/data/history_table.json","w")
    f.write(table_json)
    f.close()


def read_in_history_table(file):
    with open(file, "r") as f:
        data = f.read()

    table = json.loads(data)

    # need to re-create table with correct data-memberes, json converts keys to strings
    recreated = {True: {}, False: {}}
    t = table['true']
    f = table['false']

    t_info = {}
    for key, value in t.items():
        p_info = {int(k):v for k,v in value.items()}
        t_info[int(key)] = p_info

    f_info = {}
    for key, value in f.items():
        p_info = {int(k):v for k,v in value.items()}
        f_info[int(key)] = p_info

    recreated[True] = t_info
    recreated[False] = f_info

    return recreated