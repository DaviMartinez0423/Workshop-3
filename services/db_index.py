import json
import psycopg2
from psycopg2 import Error

def get_connection():
    try:
        with open('./services/configuration.json', encoding = 'utf-8') as f:
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
            year INTEGER,
            happiness_prediction REAL
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

def insertion(message):
    conn = None
    try:
        conn = get_connection()
        cursor = conn.cursor()
        data = message
        data_tuple = (
            data.get('country'),
            data.get('happiness_score'),
            data.get('gdp_per_capita'),
            data.get('social_support'),
            data.get('life_expectancy'),
            data.get('freedom'),
            data.get('government_corruption'),
            data.get('generosity'),
            data.get('year'),
            data.get('happiness_prediction')
        )

        insert_query = '''
        INSERT INTO happiness_table (country, happiness_score, gdp_per_capita, social_support, 
                                     life_expectancy, freedom, government_corruption, generosity, year, happiness_prediction)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        '''

        cursor.execute(insert_query, data_tuple)
        print('Row inserted successfully', data_tuple)
        conn.commit()

    except Error as e:
        print("There was an error inserting the data: ", e)

    finally:
        if conn is not None:
            cursor.close()
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
