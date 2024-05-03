import pandas as pd
import joblib
from json import dumps
from kafka import KafkaProducer, KafkaConsumer
from services.db_index import insertion

model_file = '../model/random_forest_model.pkl'
joblib_file = joblib.load(model_file)


def producer(row):
    producer_kafka = KafkaProducer(
        value_serializer= lambda m: dumps(m).encode('utf-8'),
        bootstrap_servers = ['localhost:9092']
    )
    
    message = row.to_dict()
    producer_kafka.send('Hapiness Topic', value= message)
    print('The message was sent successfully')
    
def consumer():
    consumer_kafka = KafkaConsumer(
        'Hapiness Topic',
        auto_commit = True,
        group_id =  'ETL Group',
        value_serializer= lambda m: dumps(m).encode('utf-8'),
        bootstrap_servers = ['localhost:9092']        
    )   
    
    for info in consumer_kafka:
        df = pd.json_normalize(info.value)
        df['Hapiness Prediction'] = joblib_file.predict(df['freedom','gdp per capita','life expectancy','social support'])
        insertion(df.iloc[0])
        print('Information stored in the PostgreSQL database')