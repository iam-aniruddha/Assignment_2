# 4. Use the python Faker module to generate fake data for the following.
# 	a. Create an excel sheet "Employee Personal Details" with following data. Generate around 50-100 records
# 		"EMP ID", "EMP NAME", "EMP EMAIL", "Businees Unit" "Salary"

# 	4a. WAF to return the empolyee name with top most salary
# 	4b. WAF to return the Business Unit with top most aggregated salary
# 	4c. WAF to return the employee name in each Business Unit with top most salary
# 	4d. WAF Delete the Record of the Employee name from the Excel File with the least salary.
# 	4e. WAF to Update the Salary Details of an Employee in the Excel File

import pandas as pd
from faker import Faker

class EmployeeData:
    def __init__(self, num_records=100, excel_file_path="Employee_Personal_Details.xlsx"):
        self.fake = Faker(locale='en_IN')
        self.num_records = num_records
        self.excel_file_path = excel_file_path
        self.data = self.generate_employee_data()

    def generate_employee_data(self):
        employee_data = []
        for _ in range(self.num_records):
            emp_id = self.fake.unique.random_number(digits=6)
            emp_name = self.fake.name()
            emp_email = self.fake.email()
            business_unit = self.fake.random_element(elements=('HR', 'Finance', 'Engineering', 'IT', 'Sales', 'Marketing'))
            salary = self.fake.random_int(min=40000, max=120000)
            employee_data.append((emp_id, emp_name, emp_email, business_unit, salary))
        df = pd.DataFrame(employee_data, columns=["EMP ID", "EMP NAME", "EMP EMAIL", "Business Unit", "Salary"])
        df.to_excel(self.excel_file_path, index=False)
        return df

    def get_top_salary_employee(self):
        top_salary_row = self.data[self.data["Salary"] == self.data["Salary"].max()]
        return top_salary_row["EMP NAME"].iloc[0]

    def get_top_aggregated_unit(self):
        top_unit = self.data.groupby("Business Unit")["Salary"].sum().idxmax()
        return top_unit
   
    def get_top_salary_per_unit_employee(self):
        top_salary_per_unit_employee = self.data.loc[self.data.groupby('Business Unit')['Salary'].idxmax()]
        return top_salary_per_unit_employee[["Business Unit", "EMP NAME", "Salary"]]
   
    def delete_lowest_salary_employee(self):
        lowest_salary_row = self.data[self.data["Salary"] == self.data["Salary"].min()]
        self.data.drop(lowest_salary_row.index, inplace=True)
        self.data.to_excel(self.excel_file_path, index=False)
        print("\nEmployee with the least salary is deleted.")

    def update_salary(self, emp_id, new_salary):
        if emp_id not in self.data["EMP ID"].values:
            print(f"Employee with EMP ID {emp_id} does not exist. Salary not updated.")
            return None

        self.data.loc[self.data["EMP ID"] == emp_id, "Salary"] = new_salary
        self.data.to_excel(self.excel_file_path, index=False)
        print(f"Salary updated for employee with EMP ID {emp_id}. New salary: {new_salary}")

if __name__ == "__main__":
    emp_data = EmployeeData()

    print(f"Employee with the highest salary: {emp_data.get_top_salary_employee()}")

    print(f"Business Unit with the highest aggregated salary: {emp_data.get_top_aggregated_unit()}")

    print("\nEmployee in each Business Unit with the topmost salary:")
    print(emp_data.get_top_salary_per_unit_employee())

    #  Delete the employee with the least salary
    emp_data.delete_lowest_salary_employee()

    # Example: Update salary for employee with EMP ID 12345
    emp_data.update_salary(emp_id=12345, new_salary=80000)