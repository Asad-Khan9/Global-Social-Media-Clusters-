import pandas as pd
import json

def excel_to_json(excel_file_path, json_file_path):
    # Read Excel file
    df = pd.read_excel(excel_file_path)

    # Convert DataFrame to JSON
    json_data = df.to_json(orient='records')

    # Write JSON data to file
    with open(json_file_path, 'w') as json_file:
        json_file.write(json_data)

if __name__ == "__main__":
    excel_file_path = input("Enter the path to the Excel file: ")
    json_file_path = input("Enter the path to save the JSON file: ")
    excel_to_json(excel_file_path, json_file_path)
    print("Conversion completed. JSON file saved at:", json_file_path)
