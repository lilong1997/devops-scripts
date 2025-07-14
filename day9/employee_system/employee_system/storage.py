# storage.py
import os
import json

FILE = "data.json"

def load_data():
    if not os.path.exists(FILE):
        return []
    else:
        with open(FILE, 'r', encoding='utf-8') as f:
            return json.load(f)

def save_data(data):
    with open(FILE, 'w', encoding='utf-8') as f:
        return json.dump(data, f, ensure_ascii=False, indent=2)