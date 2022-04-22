import re
import pandas as pd
def transform_vietnamese(text: str) -> str:
    """
    Convert from 'Tieng Viet co dau' thanh 'Tieng Viet khong dau'
    text: input string to be converted
    Return: string converted
    """

    patterns = {
    '[àáảãạăắằẵặẳâầấậẫẩ]': 'a',
    '[đ]': 'd',
    '[èéẻẽẹêềếểễệ]': 'e',
    '[ìíỉĩị]': 'i',
    '[òóỏõọôồốổỗộơờớởỡợ]': 'o',
    '[ùúủũụưừứửữự]': 'u',
    '[ỳýỷỹỵ]': 'y'
    }

    output = text
    for regex, replace in patterns.items():
        output = re.sub(regex, replace, output)
        # deal with upper case
        output = re.sub(regex.upper(), replace.upper(), output)
        
    return output

def remove_multiple_characters(text: str, pattern = r'(\_)\1+') ->  str:
    #remove multiple "_" continute
    text = re.sub(pattern, r'\1',text)
    #remove "_" character first
    if text[0] == '_':
        text = text[1:]
    #remove "_" character tail
    if text[-1] == '_':
        text = text[:-1]
    return text


def standardize(column_name: str) -> str:
    column_name_copy = column_name
    column_name_copy = transform_vietnamese(column_name_copy)
    positions = re.findall('[ .,;{}()\[\]\n\t=\/]', column_name)
    if positions != None:
        for p in positions:
            column_name_copy = column_name_copy.replace(p, '_') 
    column_name_copy = remove_multiple_characters(column_name_copy)
    return column_name_copy.lower()


def fit_by_config(columns, config_columns: dict) -> list:
    columns_changed =[]
    for col in columns:
        if col in config_columns:
            columns_changed.append(config_columns[col])
        else:
            print('Error: {} not have in config columns'.format('None' if col == None else col))
            return None
    return columns_changed


def extract(list_dataframe: list) -> list:
    list_columns = []
    for dataframe in list_dataframe:
        columns = dataframe.columns
        list_columns.extend(columns)
    return list_columns

def sort_dict(dict: dict, by = 'key') -> dict :
    
    index = 0
    if by == 'value':
        index = 1
    dict_sorted = {k: v for k, v in sorted(dict.items(), key=lambda item: item[index])}
    return dict_sorted

def extract_config_columns(list_columns, sort = True, sort_by = "key"):

    config_columns = {}
    for colname in list_columns:
        col_standard = standardize(colname)
        config_columns[colname] = col_standard
    if sort == True:
        config_columns = sort_dict(config_columns, by = sort_by)

    return config_columns

def update_new_columns(new_columns, config_columns):

    config_columns_copy = config_columns
    for colname in new_columns:
        if colname not in config_columns_copy:
            colname_standard = standardize(colname)
            config_columns_copy[colname] = colname_standard
    
    return config_columns_copy

def transform_columns(columns, config_columns: dict, update_column = True) -> list:
    
    if update_column:
        new_config_columns = update_new_columns(columns,config_columns)
        config_columns = new_config_columns
    
    columns_standard = fit_by_config(columns, config_columns)
    
    return columns_standard, new_config_columns