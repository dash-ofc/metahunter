import sys
import os
from extractors.pdf import extract_pdf_metadata
from extractors.docx import extract_docx_metadata
from reports.generate import save_to_json
from reports.html_report import save_to_html

def walk_directory(directory):
    supported_ext = ['.pdf', '.docx', '.jpg', '.jpeg', '.png']
    files = []

    for root, _, filenames in os.walk(directory):
        for file in filenames:
            if any(file.lower().endswith(ext) for ext in supported_ext):
                files.append(os.path.join(root, file))
    
    return files

def main():
    if len(sys.argv) != 2:
        print("Usage: python metahunter.py /path/to/folder")
        sys.exit(1)

    target_dir = sys.argv[1]

    if not os.path.isdir(target_dir):
        print("❌ Error: Path does not exist or is not a directory.")
        sys.exit(1)

    print(f"🔍 Scanning directory: {target_dir}")
    files = walk_directory(target_dir)

    print(f"✅ Found {len(files)} supported files.")

    all_metadata = []

    # PDF Metadata Extraction
    print("\n📄 Extracting metadata from PDF files...\n")
    for f in files:
        if f.lower().endswith(".pdf"):
            metadata = extract_pdf_metadata(f)
            all_metadata.append(metadata)
            print(f"\n📁 File: {metadata.get('file')}")
            if 'error' in metadata:
                print(f"❌ Error: {metadata['error']}")
            else:
                print(f"   Author   : {metadata.get('author')}")
                print(f"   Title    : {metadata.get('title')}")
                print(f"   Creator  : {metadata.get('creator')}")
                print(f"   Producer : {metadata.get('producer')}")
                print(f"   Created  : {metadata.get('created')}")

    # DOCX Metadata Extraction
    print("\n📝 Extracting metadata from DOCX files...\n")
    for f in files:
        if f.lower().endswith(".docx"):
            metadata = extract_docx_metadata(f)
            all_metadata.append(metadata)
            print(f"\n📁 File: {metadata.get('file')}")
            if 'error' in metadata:
                print(f"❌ Error: {metadata['error']}")
            else:
                print(f"   Author          : {metadata.get('author')}")
                print(f"   Title           : {metadata.get('title')}")
                print(f"   Subject         : {metadata.get('subject')}")
                print(f"   Created         : {metadata.get('created')}")
                print(f"   Last Modified By: {metadata.get('last_modified_by')}")

    # Save JSON Report
    print("\n💾 Saving metadata report...")
    report_path = save_to_json(all_metadata)
    print(f"✅ JSON report saved to: {report_path}")

    # Save HTML Report
    print("🖥️ Generating HTML report...")
    html_path = save_to_html(all_metadata)
    print(f"✅ HTML report saved to: {html_path}")

if __name__ == "__main__":
    main()
