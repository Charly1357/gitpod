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

sales = SHEET.worksheet('sales')

data = sales.get_all_values()

#print(data)
"""
  Input from the user
"""
def get_sales_data():
    print("Please enter sales from the last market ")
    print("It should be six numbers with a comma in between 1,2,3,4,5,6\n")
    data_str = input("Enter your data here")
    data_validation(data_str)

"""
  Validate the data
"""

def data_validation(data):
    sales_data = data.split(",")
    try:
       if(len(data))!=6:
          raise ValueError(f"Expected values 6 you introducen {len(data)}")

    while true:

get_sales_data()   



