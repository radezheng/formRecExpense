# Form Recognizer for MS expense

need to set Environment Variable:
``` json
            "env": {
                "FORM_KEY": "xxx",
                "FORM_ENDPOINT": "https://xxx.cognitiveservices.azure.com/"
            }
 
```

Will read all file in path, and rename with Date, Amount and Merchant:
``` python
path = "C:/Users/zhzhen/OneDrive - Microsoft/Office Lens/"
# path = "C:/tools/"
fn = [filename for filename in os.listdir(path) if filename.endswith((".pdf", "jpeg", "jpg", "png", "gif"))]
```

you can scan with your office Lens, and upload to onedrive, and then use this script to rename.
