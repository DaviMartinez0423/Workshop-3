<p align="center">
  <div style="display: flex; justify-content: center; align-items: center;">
    <img width="180" src="./public/Kafka_logo1.png" alt="Kafka">
  </div>
  <h1 align="center">⚙️ Data Streaming ⚙️</h1>
</p>

Welcome. This repository contains an exercise of data streaming using Apache Kafka. The objective of the challenge is to use the datasets provided by the teacher in charge to perform a cleaning process and use this information to create a prediction model, which will be used to predict one of the columns in the datasets.

In this repository, the following platforms are utilized:
- Apache Kafka
- Docker

## System Requirements 🖥️

### Docker:
- **Operating System:** Compatible with Windows, macOS, and Linux.
- **Processor:** Should be 64-bit.
- **RAM:** At least 4 GB is recommended.
- **Virtualization:** Enable virtualization in the BIOS (such as "Intel VT-x" or "AMD-V").

### Apache Kafka:
- **64-bit Processor.**
- **RAM:** At least 4 GB is recommended.
- **ZooKeeper:** Up to version 2.8.0, Kafka relied on ZooKeeper for coordination. However, starting from version 2.8.0, Kafka supports a mode without ZooKeeper dependency.
- **Docker:** Docker images for Kafka can be used.

**If you want to run the project on your computer, please make sure that your device is compatible with these applications. If it is not, I strongly recommend that you do not run this repository.**

## Project Structure 📃
The structure of the directories and files is as follows:

<pre>

  ├── model
  │ └── random_forest_model.pkl
  ├── notebooks
  │ ├── dataset/
  │ ├── EDAs.ipynb
  │ └── Model_accuracy.ipynb
  ├── public
  │ └── Kafka_logo1.png
  ├── services
  │ ├── init.py
  │ ├── db_query.py
  │ └── kafka.py
  ├── docker-compose.yaml
  ├── kafka_consumer.py
  ├── kafka_producer.py
  ├── README.md
  └── requirements.txt
</pre>


### Folders 📁
- **model 📑:** This folder stores the predictive model.
- **dataset 📊:** Contains .csv files with the data that will be used during the workshop.
- **notebooks 📚:** This folder contains the Jupyter notebooks that contain the dataset cleaning and analysis exercises as well as the model training.
- **services 📂:** This folder contains the configuration of the Kafka service, as well as the requests to be made to the database and the exercise of cleaning the information for the subsequent execution.

In the root, we find the files for the execution of Kafka and Docker, as well as the libraries used contained in the file "requirements.txt".

## Installation Requirements ✔️
To optimize the efficiency of your computer, you can choose to create a virtual environment where you can download the libraries, this is not mandatory and you can create one with this command:

```
python -m venv venv
```

To get inside the virtual environment, use these commands:

```
cd venv
```

```
cd Scripts
```

```
activate
```
Once you have created the virtual environment (or not), execute this command to download the libraries:
```
pip install -r requirements.txt
```

Additionally, also run this command separately:
```
pip install git+https://github.com/dpkp/kafka-python.git
```

## Project Execution 🚀

1. In a terminal, enter in a folder that you want to clone the repository:
    ```
    cd your_folder
    ```

2. Clone the repository using this command:
    ```
    git clone https://github.com/DaviMartinez0423/Workshop-3.git
    ```

3. Before running it, in the folder 'services', create a JSON file called 'configuration' like this:
    ```json
    {
        "POSTGRES_USER": "postgres_name",
        "POSTGRES_PASSWORD": "your_postgres_password",
        "POSTGRES_HOST": "localhost",
        "POSTGRES_PORT": 5432,
        "POSTGRES_DB": "your_database_name"
    }
    ```
    Also, you must create the database in Postgres first, otherwise, the program will show an Exception.

4. Enter into the cloned folder, open a terminal and execute this command:
    ```
    docker compose up -d
    ```

5. If you want to make sure Docker is working, execute this command:
    ```
    docker compose ps
    ```

6. In the same command line, execute this command to access the container and create the topic:
    ```
    docker exec -it kafka bash
    ```
    ```
    kafka-topics --bootstrap-server kafka-test:9092 --create --topic happiness
    ```

7. Open two new terminals (preferably bash). In the first one, execute these commands to run the consumer (remember to be located in the root):
    ```
    python kafka_consumer.py
    ```

8. In the second terminal, execute this command to run the producer:
    ```
    python kafka_producer.py
    ```

The terminal must show the data stream. If you want to watch the model accuracy, enter the file "Model_accuracy.ipynb" in the 'notebooks' folder.

## Contact 📧
If you have any questions or need further assistance, feel free to contact me:
- [david_fel.martinez@uao.edu.co](mailto:david_fel.martinez@uao.edu.co)