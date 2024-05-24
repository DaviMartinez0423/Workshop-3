import pandas as pd
import joblib
import os
from json import dumps, loads
from kafka import KafkaProducer, KafkaConsumer
from services.db_query import insertion

model = joblib.load('C:/Users/Usuario/Workshop_3.1/Workshop-3/model/random_forest_model.pkl')
features = ['freedom', 'gdp_per_capita', 'life_expectancy', 'social_support']


def producer(row):
    producer_kafka = KafkaProducer(
        value_serializer= lambda m: dumps(m).encode('utf-8'),
        bootstrap_servers = ['localhost:9092']
    )
    
    message = row.to_dict()
    producer_kafka.send('Hapiness', value= message)
    print(message)

def consumer():
    consumer_kafka = KafkaConsumer(
        'Hapiness',
        enable_auto_commit=True,
        group_id='ETL Group',
        value_deserializer=lambda m: loads(m.decode('utf-8')),
        bootstrap_servers=['localhost:9092']
    )   
    
    for message in consumer_kafka:
        df = pd.json_normalize(data=message.value)
        X = df[features]
        prediction = model.predict(X)
        df['happiness_prediction'] = prediction
        insertion(df.to_dict(orient='records')[0])