import psycopg2

class ClassPostgreSql:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs) 

    
    def getconnection(self):

        try:
            connection = psycopg2.connect(user = "postgres",
                                            password = "PASSWORD",
                                            host = "127.0.0.1",
                                            port = "5432",
                                            database = "linkinden")
            cursor = connection.cursor()
            # Print PostgreSQL Connection properties
           # print ( connection.get_dsn_parameters(),"\n")
            # Print PostgreSQL version
            cursor.execute("SELECT version();")
            record = cursor.fetchone()
         # print("You are connected to - ", record,"\n")
            return connection
        except (Exception, psycopg2.Error) as error :
            return None
    
    def closeconnection(self,connection):
        cursor = connection.cursor()
        if(connection):
            cursor.close()
            connection.close()
         #   print("PostgreSQL connection is closed")

    def insertrowseducation(self,connection,listrecord):
        try:
            cursor = connection.cursor()
            postgres_insert_query = """ INSERT INTO education ("EDUNAME","COURSENAME","COURSEDETAILS","COURSEGRADE","COURSEFROM","COURSETO","COURSEDESCRIPTION","URL") VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""
            #record_to_insert = ('EDUNAME','COURSENAME','COURSEDETAILS','COURSEGRADE','COURSEFROM','COURSETO','COURSEDESCRIPTION')
            record_to_insert = tuple(listrecord)
            cursor.execute(postgres_insert_query, record_to_insert)
            connection.commit()
            count = cursor.rowcount
           # print (count, "Record inserted successfully into table")
        except (Exception, psycopg2.Error) as error :
            if(connection):
                print("Failed to insert record into table", error)
        finally:
    #closing database connection.
            if(connection):
                cursor.close()
                connection.close()
                #print("PostgreSQL connection is closed")

    def insertrowsexpreiance(self,connection,listrecord):
        try:
            cursor = connection.cursor()
            postgres_insert_query = """ INSERT INTO experience ("PROURL","POSITION","COMPANY","JOBFROM","JOBTO","DURATION","JOBLOATION","DESCRIPTION") VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"""
            #record_to_insert = ('EDUNAME','COURSENAME','COURSEDETAILS','COURSEGRADE','COURSEFROM','COURSETO','COURSEDESCRIPTION')
            record_to_insert = tuple(listrecord)
            cursor.execute(postgres_insert_query, record_to_insert)
            connection.commit()
            count = cursor.rowcount
           # print (count, "Record inserted successfully into table")
        except (Exception, psycopg2.Error) as error :
            if(connection):
                print("Failed to insert record into table", error)
        finally:
    #closing database connection.
            if(connection):
                cursor.close()
                connection.close()
                #print("PostgreSQL connection is closed")

    def insertpersonalinfo(self,connection,listrecord):
            try:
                cursor = connection.cursor()
                postgres_insert_query = """ INSERT INTO profileinfo ("URLPAGE","TITLE","ADDERESS","CURROCCUPATION","HEADERCOMPANY","HEADEREDUCATION","ABOUT") VALUES (%s,%s,%s,%s,%s,%s,%s)"""
                #record_to_insert = ('EDUNAME','COURSENAME','COURSEDETAILS','COURSEGRADE','COURSEFROM','COURSETO','COURSEDESCRIPTION')
                record_to_insert = tuple(listrecord)
                cursor.execute(postgres_insert_query, record_to_insert)
                connection.commit()
                count = cursor.rowcount
               # print (count, "Record inserted successfully into table")
            except (Exception, psycopg2.Error) as error :
                if(connection):
                    print("Failed to insert record into table", error)
            finally:
        #closing database connection.
                if(connection):
                    cursor.close()
                    connection.close()
                    #print("PostgreSQL connection is closed")

    def insertcrawllink(self,connection,listrecord):
                try:
                    cursor = connection.cursor()
                    postgres_insert_query = """ INSERT INTO links ("URL","STATUS") VALUES (%s,%s)"""
                    #record_to_insert = ('EDUNAME','COURSENAME','COURSEDETAILS','COURSEGRADE','COURSEFROM','COURSETO','COURSEDESCRIPTION')
                    record_to_insert = tuple(listrecord)
                    cursor.execute(postgres_insert_query, record_to_insert)
                    connection.commit()
                    count = cursor.rowcount
                # print (count, "Record inserted successfully into table")
                except (Exception, psycopg2.Error) as error :
                    if(connection):
                        print("Failed to insert record into table", error)
                finally:
            #closing database connection.
                    if(connection):
                        cursor.close()
                        connection.close()
                        #print("PostgreSQL connection is closed")

    def getlinktoprocess(self,connection):
        link = ''
        try:
            cursor = connection.cursor()
            postgreSQL_select_Query = """SELECT  links."URL" FROM   public.links where  links."STATUS" = 'NOCRAWL' order by links."STATUS" limit 1;"""
            cursor.execute(postgreSQL_select_Query)
            mobile_records = cursor.fetchall() 
            for row in mobile_records:
                link =  row[0]
                
        except (Exception, psycopg2.Error) as error :
            print ("Error while fetching data from PostgreSQL", error)
        finally:
            #closing database connection.
            if(connection):
                cursor.close()
                connection.close()
                return link
                #print("PostgreSQL connection is closed")
    
    
    def updatelinks(self,connection,status,urllink):
        try:
            cursor = connection.cursor()
            # Update single record now
            sql_update_query = """UPDATE links SET "STATUS" = %s  WHERE "URL" = %s"""
            cursor.execute(sql_update_query, (status, urllink))
            connection.commit()
            count = cursor.rowcount
            print(count, "Record Updated successfully ")
            print("Table After updating record ")
            # sql_select_query = """select * from links where STATUS = %s"""
            # cursor.execute(sql_select_query, (status,))
            # record = cursor.fetchone()
            # print(record)
        except (Exception, psycopg2.Error) as error:
            print("Error in update operation", error)
        finally:
            # closing database connection.
            if (connection):
                cursor.close()
                connection.close()
                print("PostgreSQL connection is closed")             

# cs = ClassPostgreSql()
# conn = cs.getconnection()
#cs.insertrows(conn,['test','tet','COURSEDETAILS','COURSEGRADE','COURSEFROM','COURSETO','COURSEDESCRIPTION'])
