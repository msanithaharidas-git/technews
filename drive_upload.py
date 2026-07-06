import io
import streamlit as st
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseUpload

# =====================================================
# Google Drive Folder ID
# Replace with your Google Drive folder ID
# Example:
# https://drive.google.com/drive/folders/1AbCdEfGhIjKlMnOp
# Folder ID = 1AbCdEfGhIjKlMnOp
# =====================================================
FOLDER_ID = "1IJsogdCX9KiuBB953Kp9kBRhfLIYP3vj"


def upload_to_drive(file_path, file_name=None):
    """
    Uploads a file to Google Drive using Streamlit Secrets.

    Parameters:
        file_path (str): Local path of the file.
        file_name (str): Optional name in Google Drive.

    Returns:
        str: Shareable Google Drive link.
    """

    credentials = service_account.Credentials.from_service_account_info(
        st.secrets["gcp_service_account"],
        scopes=["https://www.googleapis.com/auth/drive"]
    )

    service = build("drive", "v3", credentials=credentials)

    if file_name is None:
        file_name = file_path.split("/")[-1]

    file_metadata = {
        "name": file_name,
        "parents": [FOLDER_ID]
    }

    with open(file_path, "rb") as f:
        media = MediaIoBaseUpload(io.BytesIO(f.read()), resumable=True)

        uploaded_file = service.files().create(
            body=file_metadata,
            media_body=media,
            fields="id"
        ).execute()

    file_id = uploaded_file.get("id")

    return f"https://drive.google.com/file/d/{file_id}/view"
