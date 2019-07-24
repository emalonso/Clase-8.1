from flask import Flask,render_template
app = Flask(__name__)

@app.route('/hello/<name>')
def hello(name):
    #Coleccion
    dict= {"python":50,"java":20,"php":30}
    return render_template("hello.html", user=name, dict=dict)
    #cierre coleccion
  

if __name__ =='__main__':
    app.run(debug=True)
