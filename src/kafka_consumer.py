import kafka_consumer
from services.db_index import table_creation

if __name__ =="__main__":
    table_creation()
    kafka_consumer()