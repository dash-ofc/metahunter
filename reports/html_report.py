import os
from datetime import datetime

def save_to_html(metadata_list, output_dir="reports"):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"metahunter_report_{timestamp}.html"
    path = os.path.join(output_dir, filename)

    html = """
    <html>
    <head>
        <meta charset="utf-8">
        <title>MetaHunter Report</title>
        <style>
            body { font-family: Arial, sans-serif; padding: 20px; background: #f4f4f4; }
            h1 { color: #333; }
            .file-block {
                background: white;
                padding: 15px;
                margin: 10px 0;
                border-left: 5px solid #007BFF;
                box-shadow: 0 2px 5px rgba(0,0,0,0.1);
            }
            .key { font-weight: bold; color: #444; }
        </style>
    </head>
    <body>
        <h1>MetaHunter Report</h1>
    """

    for item in metadata_list:
        html += "<div class='file-block'>"
        for key, value in item.items():
            html += f"<p><span class='key'>{key.title()}:</span> {value}</p>"
        html += "</div>"

    html += """
    </body>
    </html>
    """

    try:
        with open(path, "w") as f:
            f.write(html)
        return path
    except Exception as e:
        return f"❌ Failed to write HTML report: {str(e)}"
