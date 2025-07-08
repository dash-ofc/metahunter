from PyPDF2 import PdfReader

def extract_pdf_metadata(filepath):
    try:
        reader = PdfReader(filepath)
        info = reader.metadata

        return {
            "file": filepath,
            "author": info.author if info.author else "Unknown",
            "title": info.title if info.title else "Unknown",
            "creator": info.creator if info.creator else "Unknown",
            "producer": info.producer if info.producer else "Unknown",
            "created": info.creation_date if info.creation_date else "Unknown"
        }

    except Exception as e:
        return {
            "file": filepath,
            "error": f"Failed to extract: {str(e)}"
        }
