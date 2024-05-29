import threading
import time
from flask import Flask, jsonify, render_template
import requests

app = Flask(__name__)

# Daftar URL perguruan tinggi swasta beserta status awalnya
urls = [
    {'url': 'https://lldikti15.kemdikbud.go.id/', 'status': 'Unknown', 'http_status': None},
    {'url': 'https://lldikti7.kemdikbud.go.id/', 'status': 'Unknown', 'http_status': None},
    {'url': 'https://anjay.co.id/', 'status': 'Unknown', 'http_status': None},
    # tambahkan hingga 45 atau lebih
]

def check_status():
    global urls
    while True:
        for url_obj in urls:
            url = url_obj['url']
            try:
                response = requests.get(url, timeout=5)
                url_obj['http_status'] = response.status_code  # Menyimpan status HTTP response
                if response.status_code == 200:
                    url_obj['status'] = 'Up'
                else:
                    url_obj['status'] = 'Down'
            except requests.RequestException:
                url_obj['status'] = 'Down'
                url_obj['http_status'] = None  # Jika terjadi kesalahan, status HTTP diatur menjadi None
        time.sleep(30)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/status', methods=['GET'])
def get_status():
    # Mengembalikan respons JSON dengan data status dan status HTTP dari setiap URL
    return jsonify({'urls': urls})

if __name__ == '__main__':
    # Jalankan thread untuk memeriksa status setiap 30 detik
    status_thread = threading.Thread(target=check_status)
    status_thread.daemon = True
    status_thread.start()

    # Jalankan aplikasi Flask
    app.run(debug=True)
