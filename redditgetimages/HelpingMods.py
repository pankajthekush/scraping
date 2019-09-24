import shutil
import smtplib
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE,formatdate
from email import encoders
import datetime


import pickle
import os.path
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

class HelpingModules():
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
    
    def makearchive(self):
        shutil.make_archive('CnH','zip',r"C:\Users\pkuma528\Desktop\py\redditgetimages\images\full")

    
    def gdriveupload(self):
        # If modifying these scopes, delete the file token.pickle.
        SCOPES = ['https://www.googleapis.com/auth/drive.metadata.readonly','https://www.googleapis.com/auth/drive.file']

        """Shows basic usage of the Drive v3 API.
        Prints the names and ids of the first 10 files the user has access to.
        """
        creds = None
        # The file token.pickle stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)

        service = build('drive', 'v3', credentials=creds)
        
        #Upload the file
        now = datetime.datetime.now()
        metadata = {'parents' : ['<FOLDERID>'],'name':str(now.day)+str(now.month)+str(now.year)+str(now.minute)+str(now.second)+'-'+'CnH.zip'}
        
        media =  {'mimeType':'application/vnd.google-apps.file' }

        res = service.files().create(body=metadata,media_body='CnH.zip',fields='id').execute()

    
