#!/usr/bin/python3

#uses the client to query the canario DB, if no query is given, the default is used

import os
from influxdb import InfluxDBClient

host = os.environ.get('INFLUXDB_HOST')
port = os.environ.get('INFLUXDB_PORT')
username = os.environ.get('INFLUXDB_USER')
password = os.environ.get('INFLUXDB_PASSWORD')
database = os.environ.get('INFLUXDB_DB')

client = InfluxDBClient(host=host, port=port, username=username, password=password, database=database)

query_default='select * from "PM2.5_BOG_FON_Hayuelos_E01" WHERE time >= now() - 10m'

print('Query ?:\n')
query=input()
if not query:
	query=query_default

result=client.query(query)

print(result)



