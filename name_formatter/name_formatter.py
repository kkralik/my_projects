# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 08:46:28 2021

@author: krali
"""

import numpy as np
import pandas as pd
import re


def create_set_of_names(filename):
    '''
    creates set of names loaded from .txt file
    parameters: filename: str, .txt file with a list of first names, e.g. "jmena.txt"
    returns: set, contains all the words from the provided file 

    '''
    names = set()
    with open(filename, 'r') as f:
        for line in f:
            names.add(line.rstrip('\n'))
    return names
   

def create_df(filename):
    '''
    converts the provided .xlsx file into DataFrame
    parameters: filename: str, full filename/ path to file, e.g. 'Table.xlsx'
    output: DataFrame
    '''
    df = pd.read_excel(filename, index_col = 'transakce')

    df = df.rename(columns = {'jméno': 'jmeno', 'příjmení': 'prijmeni', 'název účtu': 'nazev'})
    
    return df

def create_new_xlsx(df, filename):
    '''
    creates .xlsx file from dataFrame, returns NoneType
    parameters: df: DataFrame
                filename: str, desired .xlsx filename - e.g.: 'MyFile.xlsx'
    returns: None
    '''
    df = df.drop(columns = 'temp')
    df = df.rename(columns = {'jmeno': 'jméno', 'prijmeni': 'příjmení', 'nazev': 'název účtu'})
    df.to_excel(filename)
    return None

def is_name(string, first_names):
    '''
    decides whether string is in names
    parameters: string: str
                names: set of names
    returns: bool - True if yes, False if No
    '''
    if string in names:
        return True
    else:
        return False
    

def change_format(df):
    '''
    changes the data of the provided dataframe - recognises first and last name in the column 'nazev'
    and places them in columns 'jmeno' a 'prijmeni' + comments on each row for easy search of processed data
    
    parameters: df: DataFrame
    returns: DataFrame with added comments in the 'komentář' column and added first and last name, if recognised
    '''
    # change 'nazev' to first letter capital, all other lowercase
    df['temp'] = df['nazev'].str.title()
    # initialises string in 'komentář' column instead of NaN
    df['komentář'] = df['komentář'].fillna('')
    
    # create set of special characters
    special_characters = set(('!','@','#','$','%','^','&','*','(',')','-','+','?','_','=',',', '.','<','>','/'))
    
    for i in df.index:
        # split column 'nazev' to words
        slova = df.loc[i]['temp'].split()
        # skip rows where 'nazev' aren't 2 words exactly
        if len(slova) != 2:
            df.loc[df.index == i, ['komentář']] += '-- program selhal - nesprávný počet slov v názvu účtu'
            pass
        elif any(c in special_characters for c in slova[0]) or any(c in special_characters for c in slova[1]):
            df.loc[df.index == i, ['komentář']] += '-- program selhal - nepovolený znak v názvu účtu'
            pass
        else:
            if slova[0] in first_names:
                # skip rows where 'nazev' contains two first names
                if slova[1] in first_names:
                    df.loc[df.index == i, ['komentář']] += '-- program selhal - dvě křestní jména'
                    pass
                # success - 'nazev' contains lastName firstName
                else:
                    df.loc[df.index == i, ['komentář']] += '-- automaticky zpracováno'
                    df.loc[df.index == i, ['jmeno']] = slova[0]
                    df.loc[df.index == i, ['prijmeni']] = slova[1]
            # success - 'nazev' contains firstName lastName
            elif slova[1] in first_names:
                df.loc[df.index == i, ['komentář']] += '-- automaticky zpracováno'
                df.loc[df.index == i, ['jmeno']] = slova[1]
                df.loc[df.index == i, ['prijmeni']] = slova[0]
            # skip rows where 'nazev' contains no first name
            else:
                df.loc[df.index == i, ['komentář']] += '-- program selhal - chybí křestní jméno'
                pass
            
    return df


first_names = create_set_of_names('krestni-jmena.txt')
df = create_df('ilustrace_jmena-stara.xlsx')
df = change_format(df)
create_new_xlsx(df, 'ilustrace_jmena-nova.xlsx')
