

import psycopg2
import csv


def getconnection():
    pwd = input("Enter Password")
    connection = psycopg2.connect(user = "postgres",password = pwd,host = "localhost", port = "5432",database = "gmail")
    return connection

def insertemaildata(connection,record_to_insert):
    try:
        cursor = connection.cursor()
        postgres_insert_query = """ INSERT INTO EMAILDATA("MESSAGEID","CONVID","CREATEDATE","FROM","TO","SUBJECT","BODY","UDATE") VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""
        #record_to_insert = ('a','c','d','e','f','g','h','i')
        cursor.execute(postgres_insert_query, record_to_insert)
        connection.commit()
        connection.close()
    except(Exception ,psycopg2.errors.UniqueViolation) as error:

        connection.close()
        if psycopg2.errors.UniqueViolation:
            return False
        else:
            return False
    return True



def insert_data():
    data = []

    connection = getconnection()

    try:
        with open("localdb.csv",encoding='utf-8-sig',mode="a") as file:
            data = csv.reader(file)    
            for row in data:
                inputdata = tuple(row)
                inresult = insertemaildata( connection, inputdata)
                print(inresult)
            connection.close()
    except Exception as error:
        connection.close()                
        raise error
insert_data()


