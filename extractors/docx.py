from docx import Document

def extract_docx_metadata(filepath):
    try:
        doc = Document(filepath)
        core_props = doc.core_properties

        return {
            "file": filepath,
            "author": core_props.author or "Unknown",
            "title": core_props.title or "Unknown",
            "subject": core_props.subject or "Unknown",
            "created": str(core_props.created) or "Unknown",
            "last_modified_by": core_props.last_modified_by or "Unknown"
        }

    except Exception as e:
        return {
            "file": filepath,
            "error": f"Failed to extract: {str(e)}"
        }
