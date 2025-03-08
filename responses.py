import os
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# readability variable
credentials_file = "valid-micron-453004-t0-10eb96d1c336.json"

# readability variable
scopes = ['https://www.googleapis.com/auth/spreadsheets.readonly']

def get_sheet_data():

  # defines the credentials as an object drawing from a service account file, it uses my file, and my specified scope
  credentials = Credentials.from_service_account_file(credentials_file, scopes=scopes)
  
  service = build('sheets', 'v4', credentials = credentials)
  
  spreadsheet_id = '1FQLQOPDYSjrC9ouPKXIGYEie4jtzRTa_23K6WZ4sAG8'
  
  range_name = "test!A2:D2"
  
  try:
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId = spreadsheet_id, range = range_name).execute()
    values = result.get('values',[])
  
    if not values:
      print('No data found.')
    
    else:
      for row in values:
        print(f'Subject: {row[0]}, Level: {row[1]}, Availablity: {row[2]}')
  
  except HttpError as error:
    print(f'An error occurred: {error}')