# It's necessary to create a project in google cloud. 
#Install gcloud
#Login with the command "gcloud auth application-default login"

# Imports the Google Cloud Translation library
from google.cloud import translate


# Initialize Translation client
def translate_HTML_File(file, project_id="seismic-machine-380420"):
    """Translating File."""
    with open(file, "rb") as document:
        document_content = document.read()
    
    client = translate.TranslationServiceClient()
    
    location = "global"

    parent = f"projects/{project_id}/locations/{location}"
    # Translate HTML file from English to Hindi
    # Detail on supported types can be found here:
    # https://cloud.google.com/translate/docs/supported-formats
    response = client.translate_text(
        request={
            "parent": parent,
            "contents": [document_content],
            "mime_type": "text/html",  # mime types: text/plain, text/html
            "source_language_code": "en-US",
            "target_language_code": "hi",
        }
    )
    
    with open(file, "w") as newFile:
        # Save the file
        for translation in response.translations:        
            newFile.write("{}".format(translation.translated_text))
    
    return response.translations

