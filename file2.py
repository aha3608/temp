import csv
import oracledb

# Database credentials
DB_USER = "your_username"
DB_PASSWORD = "your_password"
DB_HOST = "your_host"
DB_PORT = "1521"  # Default port for Oracle
DB_SERVICE = "your_service_name"

# Function to execute SQL with CSV values
def execute_sql_with_csv(csv_file_path, sql_statement):
    try:
        # Connect to the Oracle database
        connection = oracledb.connect(
            user=DB_USER,
            password=DB_PASSWORD,
            dsn=f"{DB_HOST}:{DB_PORT}/{DB_SERVICE}"
        )
        cursor = connection.cursor()

        # Read CSV file
        with open(csv_file_path, "r") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            
            # Process each row in the CSV file
            for row in csv_reader:
                # Extract values from the key-value pairs
                values = list(row.values())
                
                if len(values) != 10:
                    raise ValueError("CSV row does not contain exactly 10 values.")
                
                # Execute the SQL statement
                cursor.execute(sql_statement, values)
        
        # Commit the transaction
        connection.commit()
        print("Data has been successfully inserted into the database.")
    
    except oracledb.DatabaseError as e:
        print(f"Database error occurred: {e}")
    
    except Exception as e:
        print(f"Error occurred: {e}")
    
    finally:
        # Close the database connection
        if cursor:
            cursor.close()
        if connection:
            connection.close()

# Example usage
if __name__ == "__main__":
    # Path to the CSV file
    csv_file_path = "data.csv"
    
    # SQL statement (example for inserting into a table with 10 columns)
    sql_statement = """
        INSERT INTO your_table_name (column1, column2, column3, column4, column5, column6, column7, column8, column9, column10)
        VALUES (:1, :2, :3, :4, :5, :6, :7, :8, :9, :10)
    """
    
    # Call the function
    execute_sql_with_csv(csv_file_path, sql_statement)
