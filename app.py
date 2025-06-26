# app.py
import gradio as gr
from extract_text import pdf_text
from test_spacy import medicine_list
from automate import run as automate_run, close_browser

def process_pdf(pdf_file):
    logs = []
    content = pdf_text(pdf_file.name)
    logs.append("Text extracted successfully.")
    
    medicines = medicine_list(content)
    logs.append(f"Medicines found: {medicines}")

    for log in automate_run(medicines):
        logs.append(log)
        yield "\n".join(logs)

def close_browser_ui():
    result = close_browser()
    return result

with gr.Blocks() as demo:

    gr.Markdown(
    """
    # Smart Pharmacy Assistant
    ###  Smart Prescription Parsing and Pharmacy Automation Solution

    This tool automates the process of ordering medicines directly from prescription PDFs.
    Using a custom-trained spaCy NER model, it accurately extracts medicine names from uploaded prescriptions. The app then automates 
    the online pharmacy workflow using Playwright by launching a browser, searching for the identified medicines, and adding them to 
    the cart, saving time and reducing manual effort. With real-time progress logging, this solution enhances efficiency in 
    pharmaceutical procurement.

    """)
    # Smart Pharmacy Assistant is an AI-powered application that streamlines the process of ordering medicines from prescription PDFs. 

    with gr.Row():
        with gr.Column(scale=1.3):
            file_input = gr.File(label="Upload Prescription PDF")
            gr.Markdown("# Run Automation")
            submit_btn = gr.Button("Start browser")
            close_btn = gr.Button("Close Browser")
            close_status = gr.Textbox(label="Browser Status", interactive=False)
        
        with gr.Column(scale=1.5):
            log_output = gr.Textbox(lines=20, label="Progress Log", interactive=False)

    submit_btn.click(fn=process_pdf, inputs=file_input, outputs=log_output)
    close_btn.click(fn=close_browser_ui, outputs=close_status)

if __name__ == "__main__":
    demo.launch()
