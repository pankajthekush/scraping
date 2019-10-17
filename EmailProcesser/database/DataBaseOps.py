



import psycopg2

def getconnection():
    connection = psycopg2.connect(user = "postgres",password = "PASSWORD",host = "localhost", port = "5432",database = "gmail")
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
            print("Unique key violation")
            connection.close()
        else:
            raise error
            connection.close()
        
def ts():
    conn = getconnection()
    insertemaildata(conn)


ts()



