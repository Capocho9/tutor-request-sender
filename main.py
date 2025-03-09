from flask import Flask
from handler import get_sheet_data

app = Flask(__name__)

@app.route('/')
def home():
    return 'Server Online'

@app.route('/form-submit', methods=['POST'])
def process():
    get_sheet_data()
    return 'Form Submitted'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)