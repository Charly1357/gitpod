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
    print(surplus_data)
    






def main():
   value = get_sales_data()
   sales = [int(values)for values in value]
   update_sales_worksheet(sales)
   calculate_surplus(sales)


main() 



