import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('gitpod')


"""
  Input from the user
"""
def get_sales_data():

  while True:
    print("Please enter sales from the last market ")
    print("It should be six numbers with a comma in between 1,2,3,4,5,6\n")

    data_str = input("Enter your data here: ")

    sales_data = (data_str.split(","))


    if data_validation(sales_data):
         print('Data is valid')
         break
     
  return sales_data    

"""
  Validate the data
"""

def data_validation(data):
    try:
       [int(values)for values in data]
       if(len(data))!= 6:
          raise ValueError (f"Expected 6 values  required you introduces {len(data)}")
    except ValueError as e:
       print(f"Invalid data: {e},please try again\n")
       return False
    
    return True

def update_sales_worksheet(data):

    """
    Add new row to your sales data
    """
    print("Update sales worksheet\n")
    sales_worksheet = SHEET.worksheet("sales")
    sales_worksheet.append_row(data)
    print("Salessheet updated succesfully\n")

def calculate_surplus(data):
    """
    Calculating the surplus data by substraction
    of stock minus sales
    """
    sales = SHEET.worksheet("stock").get_all_values()
    sales_row = sales[-1]
    sala =[int(values)for values in sales_row]
    surplus_data = []
    for sales ,date in zip(sala,data):
        surplus = sales - date 
        surplus_data.append(surplus)
    return surplus_data
    #surplus_sheet = SHEET.worksheet("surplus")
    #surplus_sheet.append_row(surplus_data)
    #print("Surplussheet updated succesfully\n")
    
def update_data(sheet,data):
    sales = SHEET.worksheet(sheet)
    sales.append_row(data)
    print("Sheet updated")

def get_last_5_entries_sales():
    sales =SHEET.worksheet("sales")
    columns = []
    for ind in range(1,7):
       column = sales.col_values(ind)
       columns.append(column[-5:])
    return columns

def calculating_stock_average(data):
     new_stock_data = []
     for column in data:
         int_column = [int(num)for num in column]
         average = sum(int_column)/len(int_column)
         stock_num = average * 1.10
         new_stock_data.append(round(stock_num))
     return new_stock_data
     
                                     


def main():
   value = get_sales_data()
   sales = [int(values)for values in value]
   update_data("sales",sales)
   surplus_data = calculate_surplus(sales)
   update_data("surplus",surplus_data)
   entries = get_last_5_entries_sales()
   stock_data = calculating_sales_average(entries)
   update_data("stock",stock_data)


main() 



