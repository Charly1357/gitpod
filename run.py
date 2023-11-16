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


#print(data)
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

value = get_sales_data()
print(value)
  



