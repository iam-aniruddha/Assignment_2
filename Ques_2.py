"""
2. Using the Dictionary output from assignment 1.b print the output as a Table.
 The Headers of a Table are as follows
 "Name of the Day", "Occurences", Short Form", "Name in Lower", "Name in upper", "Length"
"""

from prettytable import PrettyTable
from Ques_1 import WeekDaysAnalyzer
import decorator

@decorator.log_decorator
def create_table():
    """This function creates a table to display the names and their properties"""
    table = PrettyTable(['Day', 'Occurrences', 'Short Form', 'Name in Lower', 'Name in Upper', 'Length']) # pylint: disable=line-too-long

    analyzer = WeekDaysAnalyzer()
    for day, data in analyzer.days_dictionary().items():
        table.add_row([day, data[0], data[1], data[2], data[3], data[4]])

    return table

if __name__ == "__main__":
    data_table = create_table()
    print(data_table)
