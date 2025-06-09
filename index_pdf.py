import os
import base64
import requests

# Configuration
es_url = "http://localhost:9200/university-pdfs/_doc"
pipeline = "pdf_pipeline"
pdf_directory = "/home/eduardoneville/Desktop/UNI"  # Directory with PDFs

# Index each PDF
for root, dirs, files in os.walk(pdf_directory):
    for file in files:
        if file.endswith(".pdf"):
            file_path = os.path.join(root, file)
            with open(file_path, "rb") as f:
                pdf_data = f.read()
                encoded_data = base64.b64encode(pdf_data).decode("utf-8")
                doc = {
                    "data": encoded_data,
                    "filename": file
                }
                response = requests.post(es_url, json=doc, params={"pipeline": pipeline})
                print(f"Indexed {file}: {response.json()}")
