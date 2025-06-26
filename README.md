## pharmacy-assistant
Upload your Prescription PDF and make Payment  
Smart prescription parsing and Pharmacy automation  
Automates medicine search and adds them to cart on Pharmacy  
## How this works
You upload a prescription pdf  
Text is extracted using pymupdf  
custom trained NER Model extracts medicine names  
Playwright:  
Opens Apollo Pharmacy → Searches for medicine → Clicks "Add" → Opens Cart  
Logs show real tine progress  
You can then pay and click "Close Browser"  

## To Run
##### Install dependencies
pip install -r requirements.txt  
python -m playwright install
##### Run
python app.py
