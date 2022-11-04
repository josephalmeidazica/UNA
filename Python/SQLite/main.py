from flask import Flask, jsonify, request


app = Flask(__name__)


#Create
@app.route('/contato', methods=['POST'])
def create_contact(contato):
    insert_into("contatos",)
    return jsonify(devs), 200

@app.route('/devs/<string:lang>', methods=['POST'])
def devs_per_lang(lang):
    devs_per_lang = [dev for dev in devs if dev['lang'] == lang]
    return jsonify(devs_per_lang), 200


if __name__ == '__main__' :
    app.run(debug=True)


