# Make API request
from __future__ import print_function

import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Set Google Sheets API key
API_KEY = "AIzaSyAmCFE6ClDUoyiYiPzwVugXIwHLYwkAHWQ"

# Set sheet ID and range
SHEET_ID = "1x8f5bqDu1wFFusyks9PdG0YQF5bepwWEsuICvIzLyxY"
RANGE = "A2:A588"

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/documents.readonly']

# The ID of a sample document.
DOCUMENT_ID = SHEET_ID


def main():
    """Shows basic usage of the Docs API.
    Prints the title of a sample document.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('docs', 'v1', credentials=creds)

        # Retrieve the documents contents from the Docs service.
        document = service.documents().get(documentId=DOCUMENT_ID).execute()

        print('The title of the document is: {}'.format(document.get('title')))
    except HttpError as err:
        print(err)


if __name__ == '__main__':
    main()

import tweepy
import random
import openpyxl

# bearer token: AAAAAAAAAAAAAAAAAAAAAHe4lAEAAAAAWhyaJJ9xctyluumVKPsjF9NVBcU%3D2YnEEemv5GVeRkIXuBCeLzwB9DpyKgFqOhK9oLLcCnxNerK3BV
# Set Twitter API keys
consumer_key = "DiY3ZPk0asqUTPTipJ8YqOST0"
consumer_secret = "abDg60idJLjZQNVuu0lVL2awohSbsO83ghDyVxxSRuzq6X2Nua"
access_key = "1579841409783402496-vMpzxyG00HXkCMyBdqjsQZS1TSr26O"
access_secret = "NWAajum6A8cvTZhDn19LxBgAzC1sLVoghgI6lJ51v7frg"

# Set up authentication
auth = tweepy.OAuth1UserHandler(
    consumer_key, consumer_secret, access_key, access_secret)
api = tweepy.API(auth)

# Set base URL for API
BASE_URL = f"https://sheets.googleapis.com/v4/spreadsheets/{SHEET_ID}/values/{RANGE}"

# Set URL parameters
params = {"key": API_KEY}

# Get data from response
data = response.json()["values"]

# Choose a random piece of data from the list
tweet = random.choice(data)

# Prepend the tweet with the desired string
tweet = "Here is a random Hornets boxscore:" + tweet

# Tweet the modified tweet
api.update_status(tweet)
