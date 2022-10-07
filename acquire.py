import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import env
import os


def get_connection(db, user=env.user, host=env.host, password=env.password):
    '''This function uses credentials from an env file to log into a database'''
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'

def get_curriculum_data():
    '''The function uses the get_connection function to connect to a database and retrieve the curriculum_logs dataset'''
    return pd.read_sql('''SELECT * FROM logs as l
                        LEFT JOIN cohorts c on l.cohort_id = c.id;''', get_connection('curriculum_logs'))

def get_grocery_data():
    '''This function uses the get_connection function to connect to a database and retrieve the grocery_db dataset.'''
    return pd.read_sql('SELECT * FROM grocery_customers;', get_connection('grocery_db'))

def prep_curriculum_data():
    if os.path.isfile('curriculum.csv'):
        # If csv file exists read in data from csv file.
        df = pd.read_csv('curriculum.csv', index_col=False)     
    else:   
        # Read fresh data from db into a DataFrame
        df = get_curriculum_data()
        # Cache data
        df.to_csv('curriculum.csv')
    
    # drop columns with all nulls and columns that are not useful or have repeated information
    df = df.drop(columns=['deleted_at','slack','id'])

    # drop staff cohort
    df = df[df.cohort_id!=28]

    # fill nulls with placeholder in order to keep path and ip data
    df = df.fillna(0)
    return df