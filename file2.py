import csv

# Open the CSV file
with open('example.csv', mode='r') as file:
    # Create a CSV reader object
    csv_reader = csv.reader(file)
    
    # Loop through each row in the CSV file and print it
    for row in csv_reader:
        print(row)

