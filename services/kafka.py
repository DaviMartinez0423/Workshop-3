import pandas as pd
import joblib
import os
from json import dumps, loads
from kafka import KafkaProducer, KafkaConsumer
from services.db_index import insertion

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
        
        # if all(feature in df.columns for feature in features):
        #     # Hacer la predicción
        #     try:
        #         X = df[features]
        #         print("Datos para la predicción (X):")
        #         print(X)
        #         print(f"Tipo de modelo cargado: {type(model)}")
                
        #         # Asegurarse de que X es un DataFrame y no está vacío
        #         if isinstance(X, pd.DataFrame) and not X.empty:
        #             print("Tipo de X:", type(X))
        #             print("Contenido de X:\n", X)
                    
        #             prediction = model.predict(X)  # No es necesario el índice [0] aquí
        #             print("Predicción:", prediction)
                    
        #             # Agregar la predicción al DataFrame
        #             df['happiness_prediction'] = prediction
                    
        #             print("DataFrame con la predicción:")
        #             print(df)
                    
        #             # Insertar los datos con la predicción en la base de datos
        #             insertion(df.to_dict(orient='records')[0])  # Convertir DataFrame a diccionario
        #         else:
        #             print("X no es un DataFrame válido o está vacío")
            
        #     except Exception as e:
        #         print(f"Error al realizar la predicción: {e}")
        # else:
        #     print("Las columnas recibidas no coinciden con las características del modelo")
        #     print(df)
        # try:
        #     df['happiness_prediction'] = model.predict(df[['freedom','gdp_per_capita','life_expectancy','social_support']])
        #     print(df)
        # except Exception as e:
        #     print('Error: ', e)
        X = df[features]
        prediction = model.predict(X)
        df['happiness_prediction'] = prediction
        insertion(df.to_dict(orient='records')[0])