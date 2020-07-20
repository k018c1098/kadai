import datetime
from flask import Flask, render_template, request 

app = Flask(__name__)
a=[]

@app.route('/')
def index():
	return render_template('index6.html')

@app.route('/', methods=['POST'])
def index1():
    
    b = datetime.datetime.now()
    b = b.strftime('%m/%d %H:%M 歩数 :')

    msg = request.form.get('msg')
    a.append( b + msg )
    
    return render_template('index6.html', c = a )

if __name__ == '__main__':
	app.debug = True
	app.run()
