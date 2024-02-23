# 1. Create a Tuple with all Days of the week starting from Monday and output the following. 
#   a. A list of tuples which has the two consecutive days grouped together. 
#   b. A dictionary which has the name of the day as the key and value as a tuple with following values 
#       i. Occurrence of the day in a week (e.g. 1 for Monday, 2 for Tuesday) 
#       ii. Short form of the day (first three letters) 
#       iii. name of the day in the lower case 
#       iv. name of the day in the upper case 
#       v. length of each name 
#   c. A tuple with all the characters and their number of occurrences in each name of the day. 



class WeekDaysAnalyzer:
    def __init__(self):
        self.days_of_week = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday")

    def consecutive_days(self):
        consecutive_days = [(self.days_of_week[i], self.days_of_week[i + 1]) for i in range(len(self.days_of_week) - 1)]
        return consecutive_days

    def days_dictionary(self):
        days_dict = {}
        for i, day_name in enumerate(self.days_of_week):
            days_dict[day_name] = (i + 1, day_name[:3].title(), day_name.lower(), day_name.upper(), len(day_name))
        return days_dict

    def compute_character_occurrences(self):
        tuple_with_chars = []
        for day in self.days_of_week:
            char_count = {}
            for char in day:
                if char in char_count:
                    char_count[char] += 1
                else:
                    char_count[char] = 1
            tuple_with_chars.append((day, char_count))
        return tuple(tuple_with_chars)

if __name__ == "__main__":
    analyzer = WeekDaysAnalyzer()

    consecutive_days_result = analyzer.consecutive_days()
    print("List of tuples:\n", consecutive_days_result)

    days_dict_result = analyzer.days_dictionary()
    print("\nDays Dictionary:\n", days_dict_result)

    character_occurrences_result = analyzer.compute_character_occurrences()
    print("\nCharacter occurrences:\n", character_occurrences_result)