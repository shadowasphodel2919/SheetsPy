import gspread #https://docs.gspread.org/en/latest/
client = gspread.service_account(filename='credentials.json')
# from oauth2client.service_account import ServiceAccountCredentials

# # define credentials to access the Google Sheets API
# scope = ['https://spreadsheets.google.com/feeds',
#          'https://www.googleapis.com/auth/drive']
# creds = ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
# client = gspread.authorize(creds)


# specify the name of the spreadsheet and the sheet to write to
sheet_name = 'SheetsAPI'
worksheet_name = 'Sheet1'

# open the sheet and select the worksheet
sheet = client.open(sheet_name)
worksheet = sheet.worksheet(worksheet_name)

# # define the data to be inserted
# data = [['John', 'Doe', 25],
#         ['Jane', 'Doe', 30]]

# # write the data to the worksheet
# worksheet.insert_rows(data)


def getAllData():
    col = worksheet.get()
    return col

def addCell(row,col,value):
    worksheet.update_cell(row,col,value)

def returnCell(row,col):
    return worksheet.cell(int(row),int(col)).value

def deleteRow(row):
    print(row,"deleted")
    worksheet.delete_row(row)
