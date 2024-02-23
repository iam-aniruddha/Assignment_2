# 2. Using the Dictionary output from assignment 1.b print the output as a Table. The Headers of a Table are as follows
# "Name of the Day", "Occurences", Short Form", "Name in Lower", "Name in upper", "Length"


from Ques_1 import WeekDaysAnalyzer
from prettytable import PrettyTable

def create_table():
    
    table = PrettyTable(['Day', 'Occurrences', 'Short Form', 'Name in Lower', 'Name in Upper', 'Length'])
    
    analyzer = WeekDaysAnalyzer()
    for day, data in analyzer.days_dictionary().items():
        table.add_row([day, data[0], data[1], data[2], data[3], data[4]])
    
    return table

if __name__ == "__main__":
    table = create_table()
    print(table)