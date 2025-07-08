import json
import os
from datetime import datetime

def save_to_json(data, output_dir="reports"):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"metahunter_report_{timestamp}.json"
    path = os.path.join(output_dir, filename)

    def convert(obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        return str(obj)

    try:
        with open(path, "w") as f:
            json.dump(data, f, indent=4, default=convert)
        return path
    except Exception as e:
        return f"❌ Failed to write report: {str(e)}"
