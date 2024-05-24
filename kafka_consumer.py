import sys
sys.path.append('./..')
from services.db_query import table_creation
from services.kafka import consumer

if __name__ =="__main__":
    table_creation()
    consumer()