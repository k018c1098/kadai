import datetime
import calendar
from flask import Flask

app = Flask(__name__)
@app.route('/')

def jikan():
    dt1 = datetime.datetime.now()
    strdt1 = dt1.strftime('%m月%d日 %H時%M分')
    return strdt1

if __name__ == '__main__':
	app.debug = True
	app.run()
