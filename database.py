import mysql.connector

def InsertToDatabase(agg_tran, agg_user, agg_insur, map_insur, map_tran, map_user, top_tran, top_user, top_insur):
    try:
        print("Storing the Data in SQL Database")
        
        # Connect to MySQL server
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Hariharan@27"
        )

        if mydb.is_connected():
            print("Successfully connected to MySQL database")
            mycursor = mydb.cursor()

            mycursor.execute('CREATE DATABASE IF NOT EXISTS Phonepe')
            mycursor.execute('USE Phonepe')

            # Create and insert into tables
            tables = [
                ('aggregated_insurance', agg_insur, '''CREATE TABLE IF NOT EXISTS aggregated_insurance (
                    States VARCHAR(50),
                    Years INT,
                    Quarter INT,
                    Insurance_type VARCHAR(50),
                    Insurance_count BIGINT,
                    Insurance_amount BIGINT)''', 
                    'INSERT INTO aggregated_insurance (States, Years, Quarter, Insurance_type, Insurance_count, Insurance_amount) VALUES (%s, %s, %s, %s, %s, %s)'),
                
                ('aggregated_transaction', agg_tran, '''CREATE TABLE IF NOT EXISTS aggregated_transaction (
                    States VARCHAR(50),
                    Years INT,
                    Quarter INT,
                    Transaction_type VARCHAR(50),
                    Transaction_count BIGINT,
                    Transaction_amount BIGINT)''', 
                    'INSERT INTO aggregated_transaction (States, Years, Quarter, Transaction_type, Transaction_count, Transaction_amount) VALUES (%s, %s, %s, %s, %s, %s)'),
                
                ('aggregated_user', agg_user, '''CREATE TABLE IF NOT EXISTS aggregated_user (
                    States VARCHAR(50),
                    Years INT,
                    Quarter INT,
                    Brands VARCHAR(50),
                    Transaction_count BIGINT,
                    Percentage FLOAT)''', 
                    'INSERT INTO aggregated_user (States, Years, Quarter, Brands, Transaction_count, Percentage) VALUES (%s, %s, %s, %s, %s, %s)'),
                
                ('map_insurance', map_insur, '''CREATE TABLE IF NOT EXISTS map_insurance (
                    States VARCHAR(50),
                    Years INT,
                    Quarter INT,
                    District VARCHAR(50),
                    Transaction_count BIGINT,
                    Transaction_amount FLOAT)''', 
                    'INSERT INTO map_insurance (States, Years, Quarter, District, Transaction_count, Transaction_amount) VALUES (%s, %s, %s, %s, %s, %s)'),
                
                ('map_transaction', map_tran, '''CREATE TABLE IF NOT EXISTS map_transaction (
                    States VARCHAR(50),
                    Years INT,
                    Quarter INT,
                    District VARCHAR(50),
                    Transaction_count BIGINT,
                    Transaction_amount FLOAT)''', 
                    'INSERT INTO map_transaction (States, Years, Quarter, District, Transaction_count, Transaction_amount) VALUES (%s, %s, %s, %s, %s, %s)'),
                
                ('map_user', map_user, '''CREATE TABLE IF NOT EXISTS map_user (
                    States VARCHAR(50),
                    Years INT,
                    Quarter INT,
                    Districts VARCHAR(50),
                    RegisteredUser BIGINT,
                    AppOpens BIGINT)''', 
                    'INSERT INTO map_user (States, Years, Quarter, Districts, RegisteredUser, AppOpens) VALUES (%s, %s, %s, %s, %s, %s)'),
                
                ('top_insurance', top_insur, '''CREATE TABLE IF NOT EXISTS top_insurance (
                    States VARCHAR(50),
                    Years INT,
                    Quarter INT,
                    Pincodes INT,
                    Transaction_count BIGINT,
                    Transaction_amount BIGINT)''', 
                    'INSERT INTO top_insurance (States, Years, Quarter, Pincodes, Transaction_count, Transaction_amount) VALUES (%s, %s, %s, %s, %s, %s)'),
                
                ('top_transaction', top_tran, '''CREATE TABLE IF NOT EXISTS top_transaction (
                    States VARCHAR(50),
                    Years INT,
                    Quarter INT,
                    Pincodes INT,
                    Transaction_count BIGINT,
                    Transaction_amount BIGINT)''', 
                    'INSERT INTO top_transaction (States, Years, Quarter, Pincodes, Transaction_count, Transaction_amount) VALUES (%s, %s, %s, %s, %s, %s)'),
                
                ('top_user', top_user, '''CREATE TABLE IF NOT EXISTS top_user (
                    States VARCHAR(50),
                    Years INT,
                    Quarter INT,
                    Pincodes INT,
                    RegisteredUser BIGINT)''', 
                    'INSERT INTO top_user (States, Years, Quarter, Pincodes, RegisteredUser) VALUES (%s, %s, %s, %s, %s)')
            ]

            for table_name, dataframe, create_query, insert_query in tables:
                print(f"Creating table {table_name}")
                mycursor.execute(create_query)
                mydb.commit()
                
                for index, row in dataframe.iterrows():
                    values = tuple(row)
                    mycursor.execute(insert_query, values)
                
                mydb.commit()
            
        return "Data stored in the Database"
    
    except Exception as e:
        print(f"An error occurred: {e}")
    
    finally:
        if mycursor:
            mycursor.close()
        if mydb.is_connected():
            mydb.close()