import os
import json
from tika import parser
from pathlib import Path

def extract_pdf_text(pdf_directory, output_directory):
    """
    Extract text and metadata from PDFs in the given directory using Tika.
    Save extracted data as JSON files in the output directory.
    """
    # Create output directory if it doesn't exist
    os.makedirs(output_directory, exist_ok=True)
    
    # Iterate through all PDF files in the directory
    for pdf_file in Path(pdf_directory).glob("*.pdf"):
        try:
            print(f"Processing {pdf_file.name}...")
            # Parse PDF with Tika
            parsed = parser.from_file(str(pdf_file))
            
            # Extract text and metadata
            text = parsed.get("content", "").strip()
            metadata = parsed.get("metadata", {})
            
            # Create a document for OpenSearch
            doc = {
                "file_name": pdf_file.name,
                "text": text,
                "metadata": {
                    "title": metadata.get("title", ""),
                    "author": metadata.get("Author", ""),
                    "creation_date": metadata.get("Creation-Date", ""),
                    "page_count": metadata.get("xmpTPg:NPages", "")
                }
            }
            
            # Save extracted data as JSON
            output_file = os.path.join(output_directory, f"{pdf_file.stem}.json")
            with open(output_file, "w", encoding="utf-8") as f:
                json.dump(doc, f, ensure_ascii=False, indent=2)
            print(f"Saved extracted data to {output_file}")
            
        except Exception as e:
            print(f"Error processing {pdf_file.name}: {str(e)}")

if __name__ == "__main__":
    # Define input and output directories
    PDF_DIRECTORY = "/home/eduardoneville/Desktop/UNI/"  # Directory containing PDFs
    OUTPUT_DIRECTORY = "./extracted_data"  # Directory to save JSON files
    
    # Run extraction
    extract_pdf_text(PDF_DIRECTORY, OUTPUT_DIRECTORY)
