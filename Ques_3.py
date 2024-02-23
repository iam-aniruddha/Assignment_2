# 3. Write the output table from assignment 2 into an Excel File (not CSV).

import pandas as pd
from Ques_2 import create_table  # Import the create_table function

def save_to_excel(filename):
    table = create_table()  # Get the table data from Ques_2
    df = pd.DataFrame(table._rows, columns=table.field_names)
    df.to_excel(filename, index=False)  # Save the dataframe to an Excel file

if __name__ == "__main__":
    output_filename = "saved_file.xlsx"
    save_to_excel(output_filename)
    print(f"Data saved to {output_filename}")