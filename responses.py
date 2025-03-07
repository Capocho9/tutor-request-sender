import os
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

def get_service(api_name, api_version, scopes, key_file_location):
    """Get a service that communicates to a Google API.
    
    Args:
        api_name: The name of the api to connect to.
        api_version: The api version to connect to.
        scopes: A list of scopes needed for the service.
        key_file_location: The path to a valid service account JSON key file.
        
    Returns:
        A service that is connected to the specified API.
    """
    credentials = Credentials.from_service_account_file(
        key_file_location, scopes=scopes)

    # Build the service object.
    service = build(api_name, api_version, credentials=credentials)

    return service