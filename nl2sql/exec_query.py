from pyhive import hive
import logging 

def execute_query(query):
        try:
                logging.info("Connecting to Hive Metastore")
                conn = hive.Connection(host="localhost", port=10000, username='root')
                cursor = conn.cursor()
                
                logging.info("Connecting to database 'vdt'")
                cursor.execute("USE vdt")

                query = query.rstrip(';')
                logging.info(f"Executing query: {query}")
                cursor.execute(query)

        #         Fetch column names
                columns = [desc[0] for desc in cursor.description]
                result = cursor.fetchall()

                result_dict = []
                result_dict = [dict(zip(columns, row)) for row in result]
                conn.close()
                return result_dict
                
        



        except Exception as e:
                print(f"Error executing query at {e}")
                return None
        