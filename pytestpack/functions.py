import pandas as pd
import json


pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 2000)
pd.set_option('display.float_format', '{:20,.2f}'.format)
pd.set_option('display.max_colwidth', None)


def append(json_data):
    dfs = []
    for data in json_data:
        file_url = data[0]
        df = pd.read_csv(file_url)
        columns_to_rename = {item['name']: item['target'] for item in data[1:] if item['selected']}
        df.rename(columns=columns_to_rename, inplace=True)
        dfs.append(df[columns_to_rename.values()])

    result = pd.concat(dfs, ignore_index=True)
    return result


def getcolumns(urls):
    data_dict = {}
    for url in urls:
        df = pd.read_csv(url, encoding="utf-8")
        columns = df.columns.to_list()
        data_dict[url] = {"columns": columns}

    return json.dumps(data_dict)


def add(x, y):
    return x + y


def sub(x, y):
    return x - y
