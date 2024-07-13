from pymongo.mongo_client import MongoClient
import pandas as pd
import json

uri = "mongodb+srv://vanshgarg441:jALrM7C6TL7r4zU3@cluster0.klt4c9w.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
# Create a new client and connect to the server
#uri = uniform resource identifier

client = MongoClient(uri)

#create database name 
DATABASE_NAME = 'vansh_wafer'
COLLECTION_NAME = "waferfault"

#dump the data into database


# Send a ping to confirm a successful connection
df = pd.read_csv("D:\Data Science\Wafer_fault_detection_project\Wafer_fault_detection\sensor2-main\notebooks\wafer_23012020_041211.csv")
df=df.drop("Unnamed: 0",axis=1)


json_record=list(json.loads(df.T.to_json()).values())




#dump the data into database
client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)


