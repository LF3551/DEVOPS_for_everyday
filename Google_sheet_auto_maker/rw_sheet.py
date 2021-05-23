from googleapiclient.discovery import build

from google.oauth2 import service_account

SERVICE_ACCOUNT_FILE = 'C:\python_data\keys.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
# The ID spreadsheet.
creds = None
creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

def read_sheets(where_read, SPREADSHEET_ID):
    service = build('sheets', 'v4', credentials=creds)
    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SPREADSHEET_ID,
                                range=where_read).execute()
    values = result.get('values', [])
    return values


def write_final_result(to_write = [[""]], where_to_write="Sheet1!A1:H2", SPREADSHEET_ID= ""):
    service = build('sheets', 'v4', credentials=creds)
    # Call the Sheets API
    sheet = service.spreadsheets()
    request = sheet.values().append(spreadsheetId=SPREADSHEET_ID, range=where_to_write, 
                                valueInputOption="USER_ENTERED", body={"values": to_write}).execute()
    return "ok"

