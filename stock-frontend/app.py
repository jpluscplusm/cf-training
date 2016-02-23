from flask import Flask
import requests
import os

app = Flask(__name__)
port = int(os.getenv('PORT', 8080))
stock_api = os.getenv('STOCK_API_URI')

def stock_colour(level):
    if level == 0:
      return "red"
    elif level < 11:
      return "yellow"
    else:
      return "green"

@app.route('/')
def homepage():
    return "Try a /p/<ProductCode> path instead ..."

@app.route('/p/<pCode>')
def show_stock(pCode):

    response = requests.get(stock_api + '/p/' + pCode).json()
    stock_level = response['stock']
    colour = stock_colour(stock_level)

    html = '''<DOCTYPE html><html><head></head>
	<body style="background-color: {}">
	<h1>Product code: {}</h1>
	<h2>Stock level: {}</h2>
	</body></html>'''.format(colour, pCode, stock_level)

    return html

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
