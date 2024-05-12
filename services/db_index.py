import json
import psycopg2
from psycopg2 import Error

def get_connection():
    try:
        with open('C:/Users/Usuario/Workshop_3.1/Workshop-3/services/configuration.json', encoding = 'utf-8') as f:
            config = json.load(f)
            conn =  psycopg2.connect(
                
                user = config['POSTGRES_USER'],
                password = config['POSTGRES_PASSWORD'],
                host = config['POSTGRES_HOST'],
                port = config['POSTGRES_PORT'],
                database = config['POSTGRES_DB'],
                         
            )
        print('Connection with the Database done')
        return conn
    
    except psycopg2.Error as e:
        print('Connection with the database failed: ', e)
        return None


def table_creation():
    create_table_query = """
        CREATE TABLE IF NOT EXISTS happiness_table(
            country VARCHAR(255),
            happiness_score REAL,
            gdp_per_capita REAL,
            social_support REAL,
            life_expectancy REAL,
            freedom REAL,
            government_corruption REAL,
            generosity REAL,
            year INTEGER
        )
    """
    
    conn = None
    
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(create_table_query)
        cursor.close()
        conn.commit()
        
    except Error as e:
        print("There was an error creating the table: ", e)
        
    finally:
        if conn is not None:
            conn.close()

def insertion(row):
    index = '''
        INSERT INTO happiness_table(country, happiness_score, gdp_per_capita, social_support, freedom, life_expectancy, generosity, year)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    '''
    conn = None
    
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(index, row)
        cursor.close()
        conn.commit()
        
    except Error as e:
        print("There was an error inserting the data: ", e)
        
    finally:
        if conn is not None:
            conn.close()

def importation():
    query = f'''SELECT *
    FROM happiness_table
    '''
    conn = None
    
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(query)
        cursor.close()
        conn.commit()
        
    except Error as e:
        print("There was an error importing the data: ", e)
        
    finally:
        if conn is not None:
            conn.close()
