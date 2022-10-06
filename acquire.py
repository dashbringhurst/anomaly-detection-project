import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import env

def get_connection(db, user=env.user, host=env.host, password=env.password):
    '''This function uses credentials from an env file to log into a database'''
    return f'mysql+pymysql://{user}:{password}@{host}/{db}'

def get_curriculum_data():
    '''The function uses the get_connection function to connect to a database and retrieve the curriculum_logs dataset'''
    return pd.read_sql('SELECT * FROM logs;', get_connection('curriculum_logs'))

def get_grocery_data():
    '''This function uses the get_connection function to connect to a database and retrieve the grocery_db dataset.'''
    return pd.read_sql('SELECT * FROM grocery_customers;', get_connection('grocery_db'))