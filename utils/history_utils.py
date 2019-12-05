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
    return table