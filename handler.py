import os
from re import X
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from sender import contact_tutors
from finder import find_tutors

# readability variable
credentials_file = os.environ.get('google_creds')

# readability variable
scopes = ['https://www.googleapis.com/auth/spreadsheets.readonly']

def get_sheet_data():

  # defines the credentials as an object drawing from a service account file, it uses my file, and my specified scope
  credentials = Credentials.from_service_account_file(credentials_file, scopes=scopes)

  # create a google sheets api client, specify we're working with sheets, use version 4, use credentials for access
  service = build('sheets', 'v4', credentials = credentials)

  # readability variable
  spreadsheet_id = '1FQLQOPDYSjrC9ouPKXIGYEie4jtzRTa_23K6WZ4sAG8'

  # readability variable
  range_name = "'NHS Tutor Requests'!B2:E100"

  try:
    # make an api client object specifically for spreadsheets
    sheet = service.spreadsheets()

    # using the api, get a resource object that allows you to make a request to interact with values (values reads data for the api, not for you, it just     makes the computer look at the values, then it says "now what"), specify that we want to get them, say from which sheet, and in which range, this         completes the request, which we then send to the api
    result = sheet.values().get(spreadsheetId = spreadsheet_id, range = range_name).execute()

    # we just got a response object that contains the values, among other things, we specify that we only want the values (or allows it to return nothing     if there's no "values" key), and set an empty list as a failsafe if there's nothing
    values = result.get('values',[])

    if not values:
      print('No data found.')

    else:
      for row in values:
        subject = row[0]
        level = row[1]
        times = row[2]
        email = row[3]

        availability = []

        times = times.split(',')
        
        for time in times:
          availability.append(time.strip())

        tutors = find_tutors(subject,level,availability)

        contact_tutors(subject,level,availability,email,tutors)

  except HttpError as error:
    print(f'An error occurred: {error}')
