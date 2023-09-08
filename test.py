#!/usr/bin/env python
# coding: utf-8
# !pip install psycopg2
import psycopg2

# python program to print "Hello World"
print("Hello World")

#establishing the connection
conn = psycopg2.connect(
   database="tfsearch_qa_db", user='tfesearchqa', password='pinkDRAGONbumpKARL1!', host='tfe-search-cluster-qa.cluster-ro-c2ggnfjugfdn.us-east-1.rds.amazonaws.com', port= '5432'
)
#Creating a cursor object using the cursor() method
cursor = conn.cursor()

#Executing an MYSQL function using the execute() method
cursor.execute("select version()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()
print("Connection established to: ",data)

#Closing the connection
conn.close()
