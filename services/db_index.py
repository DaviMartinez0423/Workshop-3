import pandas as pd
import json
import psycopg2
from psycopg2 import Error

def conn():
    try:
        with open('../config.json', encoding = 'utf-8') as f:
            config = json.load(f)
            conn =  psycopg2.connect(
                
                user = config['POSTGRES_USER'],
                password = config['POSTGRES_PASSWORD'],
                host = config['POSTGRES_HOST'],
                port = config['POSTGRES_PORT'],
                db = config['POSTGRES_DB'],
                         
            )
        print('Connection with the Database done')
        return conn
    
    except psycopg2.Error as e:
        print('Connection with the database failed: ', e)
        return None

def table_creation():
    create_table_query = """
        CREATE TABLE IF NOT EXIST hapiness_table(
            country VARCHAR(255),
            hapiness score REAL,
            gdp per capita REAL,
            social support REAL,
            life expectancy REAL,
            freedom REAL,
            goverment corruption REAL,
            generosity REAL
            year INTEGER
        )
    """
    
    conn = None
    
    try:
        conn = conn()
        cursor = conn.cursor()
        cursor.execute(create_table_query)
        cursor.close()
        conn.commit()
        
    except Error as e:
        print("There was an error creating the table: ", e)
        
    finally:
        if conn == True:
            conn.close()

def insertion(row):
    index = '''
        INSERT INTO happiness_table(country, happiness_score, gdp_per_capita, social_support, freedom, life_expectancy, happiness_prediction)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    '''
    conn = None
    
    try:
        conn = conn()
        cursor = conn.cursor()
        cursor.execute(index)
        cursor.close()
        conn.commit()
        
    except Error as e:
        print("There was an error inserting the data: ", e)
        
    finally:
        if conn == True:
            conn.close()

def importation():
    query = f'''SELECT *
    FROM hapiness_table
    '''
    conn = None
    
    try:
        conn = conn()
        cursor = conn.cursor()
        cursor.execute(query)
        cursor.close()
        conn.commit()
        
    except Error as e:
        print("There was an error inserting the data: ", e)
        
    finally:
        if conn == True:
            conn.close()
