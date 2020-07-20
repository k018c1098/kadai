from flask import Flask, render_template

app = Flask(__name__)
c = []

@app.route('/user/')
def index():
    return render_template('index2.html')

@app.route('/user/<username>')
def tuika( username ):
    c.append(username) 
    return render_template('index2.html', massage = username + 'を追加しました')
#username + 'を追加しました'

@app.route('/user/list/')
def list():
    return render_template('index3.html', c=c ) 




if __name__ == '__main__':
    app.debug = True
    app.run()