#! /usr/bin/env python3
from influxdb import InfluxDBClient
import random
import time
random.seed()
client = InfluxDBClient(database='mydb')

while True:
	json_body = [
	    {
	        "measurement": "temperature",
	        "tags": {
	            "machine": "unit42",
	            "type": "assembly"
	        },
	        "fields": {
	            "external": random.uniform(10, 30),
	            "internal": random.uniform(25, 40),
	        }
	    },
	    {
	        "measurement": "temperature",
	        "tags": {
	            "machine": "unit21",
	            "type": "assembly"
	        },
	        "fields": {
	            "external": random.uniform(20, 35),
	            "internal": random.uniform(40, 50),
	        }
	    }
	]

	try:
		client.write_points(json_body)
	except Exception as e:
		print("Error in writing to db", e)

	time.sleep(10)

