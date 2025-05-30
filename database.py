import psycopg2


#The function used to connect database to python code
def get_connection():
    hostname="localhost"
    database="blog__app"
    username="postgres"
    pwd="131106"
    port_id=5432
    conn=None
    try:
        return psycopg2.connect(host=hostname,dbname=database,user=username,password=pwd,port=port_id)
    except Exception as error:
        print(error)
    finally:
        if conn !=None:
            conn.close()
    
