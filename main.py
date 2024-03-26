"""
This code sample shows Custom Model operations with the Azure Form Recognizer client library. 
The async versions of the samples require Python 3.6 or later.

To learn more, please visit the documentation - Quickstart: Form Recognizer Python client library SDKs v3.0
https://docs.microsoft.com/en-us/azure/applied-ai-services/form-recognizer/quickstarts/try-v3-python-sdk
"""

import os
from dotenv import load_dotenv

from azure.core.credentials import AzureKeyCredential
from azure.ai.formrecognizer import DocumentAnalysisClient

load_dotenv()

endpoint = os.getenv("FORM_ENDPOINT")
key = os.getenv("FORM_KEY")
model_id = "msexpense1229"

document_analysis_client = DocumentAnalysisClient(
    endpoint=endpoint, credential=AzureKeyCredential(key)
)

# Make sure your document's type is included in the list of document types the custom model can analyze

def rmspace(text):
    if(text is None ):
        return "none"
    if(isinstance(text, int) or isinstance(text, float)):
        return text
    text = text.replace("：", "").replace(",","").replace("，","")
    text = text.replace(")", "").replace(":","").replace("/","_")
    text = text.replace("(", "").replace("（", "").replace("）", "").replace("¥", "")
    return text.replace(" ", "")


path = "/Users/radezheng/OneDrive - Microsoft/Office Lens"
# path = "C:/tools/"
fn = [filename for filename in os.listdir(path) if filename.endswith((".pdf", "jpeg", "jpg", "png", "gif"))]
print(fn)

for f in fn:
    fall = os.path.join(path, f)
    with open(fall, 'rb') as fp:
        fb = fp.read()
    poller = document_analysis_client.begin_analyze_document(model_id, fb)
    result = poller.result()

    for idx, document in enumerate(result.documents):
        print("--------Analyzing document #{}-{}-------".format(idx + 1, f))
        # print("Document has type {}".format(document.doc_type))
        # print("Document has confidence {}".format(document.confidence))
        # print("Document was analyzed by model with ID {}".format(result.model_id))
        fname = ""
        for name, field in document.fields.items():
            
            field_value = rmspace(field.value if field.value else field.content)
            fname = fname + "{}_".format(field_value)
            # print("......value '{}'".format(field_value))
        fname = fname + os.path.splitext(f)[-1]
        print("fname: {}".format(fname))
        os.rename(fall, os.path.join(path, fname))


print("-----------------------------------")
