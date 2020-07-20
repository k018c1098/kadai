from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index4.html')
    
@app.route('/send', methods=['POST'])
def send():
    msg = request.form.get('msg')
    msg1 = request.form.get('msg1')
    return render_template('index5.html', msg=msg , msg1=msg1)

if __name__ == '__main__':
	app.debug = True
	app.run()
