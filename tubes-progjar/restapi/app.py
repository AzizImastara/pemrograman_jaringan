import threading
import time
import json
from datetime import datetime
from flask import Flask, jsonify, render_template
import requests

app = Flask(__name__)

# Fungsi untuk membaca URL dari file .json dan menginisialisasi status
def load_urls_from_file(file_path):
    urls = []
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            for item in data['data']:
                urls.append({
                    'name': item['name'], 
                    'url': item['url'], 
                    'status': 'Unknown', 
                    'last_check_up': 'Unknown'
                })
    except Exception as e:
        print(f"Error reading file: {e}")
    return urls

# Daftar URL perguruan tinggi swasta beserta status awalnya
urls = load_urls_from_file('urls.json')

# Fungsi untuk memeriksa status setiap URL secara independen
def check_status_independently(url_obj):
    while True:
        url = url_obj['url']
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                url_obj['status'] = 'Up'
                url_obj['last_check_up'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            else:
                url_obj['status'] = 'Down'
        except requests.RequestException:
            url_obj['status'] = 'Down'
        
        # Tentukan interval berdasarkan status
        interval = 60 if url_obj['status'] == 'Up' else 30
        time.sleep(interval)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/status', methods=['GET'])
def get_status():
    # Sort urls so that 'Down' statuses appear first
    sorted_urls = sorted(urls, key=lambda x: x['status'] == 'Up')
    return jsonify({'urls': sorted_urls})

if __name__ == '__main__':
    # Jalankan thread terpisah untuk setiap URL
    for url_obj in urls:
        thread = threading.Thread(target=check_status_independently, args=(url_obj,))
        thread.daemon = True
        thread.start()

    # Jalankan aplikasi Flask
    app.run(debug=True)
