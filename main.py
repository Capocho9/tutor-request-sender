from flask import Flask
from responses import get_sheet_data

app = Flask(__name__)

@app.route('/')
def home():

    get_sheet_data()
  
    return 'Server Online'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=81)