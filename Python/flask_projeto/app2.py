from flask import Flask
from flask import render_template
from flask import jsonify
from flask import request

app = Flask(__name__)


#############################################################
# RETORNANDO JSON

@app.route("/")
def index():
    return jsonify({"mensagem":"Ola mundo com JSON"})


@app.route('/soma/<int:a>/<int:b>')
def soma(a,b):
    return jsonify({"result":"%d"%(a+b)})

@app.route('/subtracao/<int:a>/<int:b>')
def sub(a,b):
    return jsonify({"result":"%d"%(a-b)})

@app.route('/multiplicacao/<int:a>/<int:b>')
def mult(a,b):
    return jsonify({"result":"%d"%(a*b)})

@app.route('/divisao/<int:a>/<int:b>')
def div(a,b):
    return jsonify({"result":"%d"%(a/b)})

@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html'), 404

#############################################################

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
