"""
3. Write the output table from assignment 2 into an Excel File (not CSV).
"""
import pandas as pd
from Ques_2 import create_table  # Import the create_table function
import decorator

@decorator.log_decorator
def save_to_excel(filename):
    """
    This function saves the output of assignment 2 to an excel file.
    """
    table = create_table()  # Get the table data from Ques_2
    df = pd.DataFrame(table._rows, columns=table.field_names) # pylint: disable=protected-access
    df.to_excel(filename, index=False)  # Save the dataframe to an Excel file

if __name__ == "__main__":
    OUTPUT_FILENAME = "saved_file.xlsx"
    save_to_excel(OUTPUT_FILENAME)
    print(f"Data saved to {OUTPUT_FILENAME}")
