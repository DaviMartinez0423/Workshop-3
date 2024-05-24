<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Videogames Data Streaming</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 20px;
        }
        .container {
            text-align: center;
        }
        .flex-container {
            display: flex;
            justify-content: center;
            align-items: center;
            margin-bottom: 20px;
        }
        .flex-container img {
            width: 180px;
            margin: 0 10px;
        }
        pre {
            background-color: #f4f4f4;
            color: #000000;
            padding: 20px;
            border: 1px solid #ccc;
            font-size: 16px;
            overflow-x: auto;
            margin-top: 10px;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="flex-container">
            <img src="./public/Kafka_logo.png" alt="Kafka">
            <img src="./public/airflow_logo.png" alt="Airflow">
        </div>
        <h1>⚙️ Videogames Data Streaming ⚙️</h1>
        <p>Welcome.</p>
		<p>
		This repository contains an exercise of data streaming using Apache Kafka.	The objective of the challenge is to use the datasets provided by the teacher in charge to perform a cleaning process and use this information to create a prediction model, which will be used to predict one of the columns in the datasets.
		</p>
        <p>In this repository, the following platforms are utilized:</p>
        <ul>
            <li>Apache Kafka</li>
            <li>Docker</li>
        </ul>
        <h2>System Requirements 🖥️</h2>
        <h3>Docker:</h3>
        <ul>
            <li><strong>Operating System:</strong> Compatible with Windows, macOS, and Linux.</li>
            <li><strong>Processor:</strong> Should be 64-bit.</li>
            <li><strong>RAM:</strong> At least 4 GB is recommended.</li>
            <li><strong>Virtualization:</strong> Enable virtualization in the BIOS (such as "Intel VT-x" or "AMD-V").</li>
        </ul>
        <h3>Apache Kafka:</h3>
        <ul>
            <li><strong>64-bit Processor.</strong></li>
            <li><strong>RAM:</strong> At least 4 GB is recommended.</li>
            <li><strong>ZooKeeper:</strong> Up to version 2.8.0, Kafka relied on ZooKeeper for coordination. However, starting from version 2.8.0, Kafka supports a mode without ZooKeeper dependency.</li>
            <li><strong>Docker:</strong> Docker images for Kafka can be used.</li>
        </ul>
        <p><strong>If you want to run the project on your computer, please make sure that your device is compatible with these applications. If it is not, I strongly recommend that you do not run this repository.</strong></p>
    </div>

    <h2>Project Structure 📃</h2>
    <p>The structure of the directories and files is as follows:</p>
    <pre>
├── model
│   └── random_forest_model.pkl
├── notebooks
│   ├── dataset/
│   ├── EDAs.ipynb
│   └── Model_accuracy.ipynb
├── public
│   └── Kafka_logo1.png
├── services
│   ├── __init__.py
│   ├── db_query.py
│   └── kafka.py
├── docker-compose.yaml
├── kafka_consumer.py
├── kafka_producer.py
├── README.md
└── requirements.txt
    </pre>

    <h2>Folders 📁</h2>
    <ul>
        <li><strong>model 📑:</strong>This folder stores the predictive model.</li>
        <li><strong>dataset 📊:</strong> Contains .csv files with the data that will be used during the workshop.</li>
        <li><strong>notebooks 📚:</strong>This folder contains the jupyter notebooks that contain the dataset cleaning and analysis exercises as well as the model training.</li>
        <li><strong>services 📂:</strong> This folder contains the configuration of the kafka service, as well as the requests to be made to the database and the exercise of cleaning the information for the subsequent execution..</li>
    </ul>

    <p>In the root we find the files for the execution of kafka and docker, as well as the libraries used contained in the file "requirements.txt".</p>

    <h2>Installation Requirements ✔️</h2>
    <p>To optimize the efficiency of your computer, you can choose to create a virtual environment where you can download the libraries, this is not mandatory and you can create one with this command:</p>
	<pre>
			python -m venv venv
	</pre>
	<p>
	To get inside the virtual enviorment, use this commands:
		</p>
	<pre>
			cd venv
	</pre>
	<pre>
			cd Scripts
	</pre>
	<pre>
			activate
	</pre>
	<p>
	Once has created the virual enviorment or not, execute this command to download the libraries:
	</p>
    <pre>
        pip install -r requirements.txt
    </pre>
    <p>Additionally, also run this command separately:</p>
	<pre>
		pip install git+https://github.com/dpkp/kafka-python.git
	</pre>

    <h2>Project Execution 🚀</h2>
    <ol>
	
	<li>In a terminal, enter in a folder that you want to clone the repository:</li>
        <pre>
            cd your_folder
        </pre>
        <li>Clone the repository using this command:</li>
        <pre>
            git clone https://github.com/DaviMartinez0423/Workshop-3.git
        </pre>
		<li>Before run it, in the folder 'services' create a json file called 'configuration' like this:</li>
		<pre>		{
		"POSTGRES_USER": "postgres_name",
		"POSTGRES_PASSWORD": "your_postgres_password",
		"POSTGRES_HOST": "localhost",
		"POSTGRES_PORT": 5432,
		"POSTGRES_DB": "your_database_name"
		}
		</pre>
		<p>
			Also, you must create the database in postgres first, in other way, the program will show an Exception
		</p>
        <li>Enter into the folder cloned, open a terminal and execute this command:</li>
        <pre>
            docker compose up -d
        </pre>
        <li>If you wanna make sure the docker is working, execute this command:</li>
		<pre>
			docker compose ps
		</pre>
        <li>In the same command line, execute this command to access the container and create the topic:</li>
        <pre>
            docker exec -it kafka bash
        </pre>
        <pre>
            kafka-topics --bootstrap-server kafka-test:9092 --create --topic happiness
        </pre>
        <li>Open two new terminals, (preferably bash) in the first one execute these commands to execute the consume (remember to be located in the root):</li>
        <pre>
            python kafka_consumer.py
        </pre>
		<li>In the second terminal execute this command to run the producer</li>
        <pre>
            python kafka_producer.py
        </pre>
        <li>The terminal must show the data stream. If you wanna watch the model accurancy, enter in the file "Model_accurancy" in the folder 'notebooks</li>
    </ol>

    <h2>Contact 📧</h2>
    <p>If you have any questions or need further assistance, feel free to contact me:</p>
    <ul>
        <li><a href="mailto:david_fel.martinez@uao.edu.co">david_fel.martinez@uao.edu.co</a></li>
    </ul>
</body>
</html>