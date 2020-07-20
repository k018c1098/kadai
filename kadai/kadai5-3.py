import datetime
from flask import Flask, render_template, request 

app = Flask(__name__)
a=[]
s=[]
h=[]

@app.route('/')
def index():
	return render_template('index7.html')

@app.route('/', methods=['POST'])
def index1():
    
    b = datetime.datetime.now()
    b = b.strftime('%m/%d %H:%M 歩数 :')

    msg = request.form.get('msg')
    a.append( b + msg )

    #リストの平均
    #h = int(msg)
    #s.append(h)
    s.append(msg)
    h = [int(d) for d in s]
    z = sum(h) / len(h)
    
    return render_template('index7.html', c = a , heikin = z)

if __name__ == '__main__':
	app.debug = True
	app.run()
