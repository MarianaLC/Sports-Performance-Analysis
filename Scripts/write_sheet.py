
from googleapiclient.discovery import build
from google.oauth2 import service_account
import adafruit_send


SERVICE_ACCOUNT_FILE = 'client_secret.json'

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
credentials = None
credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# The ID of a sample spreadsheet.
SAMPLE_SPREADSHEET_ID = '1puG327IPMaC10-_4FAry1RtuuwIL5WQjrKTkJb36Wag'


def write(lista):
    service = build('sheets', 'v4', credentials=credentials)

    # Call the Sheets API
    sheet = service.spreadsheets()
    
    request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID,range="Lara_1703!A1", valueInputOption='USER_ENTERED', body={"values":adafruit_send.lista}).execute()
    print(request)
    
    
if __name__ == '__main__':
    write()