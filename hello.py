from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello world in flask"

@app.route('/dos')
def dos():
    return "usted esta en dos"


@app.route('/tres')
def tres():
    return "usted esta en tres"



if __name__ =='__main__':
    app.run()
