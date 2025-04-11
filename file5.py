import csv
import cx_Oracle

def execute_sql_with_csv(oracle_connection, csv_file_path, sql_query):
    """
    Executes an SQL query using values from a CSV file against an Oracle database.

    Parameters:
        oracle_connection (str): Oracle connection string (e.g., "user/password@hostIP/database").
        csv_file_path (str): Path to the CSV file.
        sql_query (str): SQL query with placeholders for values (e.g., "INSERT INTO TABLE (COLUMN1, COLUMN2) VALUES (:1, :2)").
    """
    try:
        # Connect to the Oracle database
        connection = cx_Oracle.connect(oracle_connection)
        cursor = connection.cursor()
        print("Connection established.")

        # Open the CSV file and read its contents
        with open(csv_file_path, mode="r") as csv_file:
            reader = csv.reader(csv_file)
            headers = next(reader)  # Skip header row if present
            
            # Execute SQL for each row in the CSV file
            for row in reader:
                cursor.execute(sql_query, row)

        # Commit the transaction and close the connection
        connection.commit()
        print("SQL execution completed successfully.")
        
    except Exception as error:
        print(f"Error occurred: {error}")
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

# Example usage
oracle_connection = "user/password@hostIP/database"
csv_file_path = "data.csv"
sql_query = "INSERT INTO TABLE_NAME (COLUMN1, COLUMN2, COLUMN3) VALUES (:1, :2, :3)"

execute_sql_with_csv(oracle_connection, csv_file_path, sql_query)
