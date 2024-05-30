import threading
import time
from flask import Flask, jsonify, render_template
import requests

app = Flask(__name__)

# Daftar URL perguruan tinggi swasta beserta status awalnya
urls = [
    {'url': 'https://lldikti15.kemdikbud.go.id/', 'status': 'Unknown'},
    {'url': 'https://lldikti7.kemdikbud.go.id/', 'status': 'Unknown'},
    {'url': 'anjay.co.id/', 'status': 'Unknown'},
    # tambahkan hingga 45 atau lebih
]

# Fungsi untuk memeriksa status setiap URL secara independen
def check_status_independently(url_obj):
    while True:
        url = url_obj['url']
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                url_obj['status'] = 'Up'
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
    return jsonify({'urls': urls})

if __name__ == '__main__':
    # Jalankan thread terpisah untuk setiap URL
    for url_obj in urls:
        thread = threading.Thread(target=check_status_independently, args=(url_obj,))
        thread.daemon = True
        thread.start()

    # Jalankan aplikasi Flask
    app.run(debug=True)
