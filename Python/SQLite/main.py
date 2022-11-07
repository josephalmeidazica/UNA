#
#Feito por Joseph Almeida Zica
#RA: 321119144
#
#
#
#PARA MATCH PARCIAL NAS ROTAS DE BUSCA, UTILIZE /1 NO FINAL DA ROTA
#PARA MATCH EXATO NAS ROTAS DE BUSCA, UTILIZE /0 NO FINAL DA ROTA
#

from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

@app.route('/contato', methods=['POST'])
def create_contact():
    con = sqlite3.connect("agenda.db")
    cur = con.cursor()
    contato = request.get_json()
    query = ("insert into contatos (nome, empresa, email, telefone) values ('{0}','{1}','{2}','{3}')").format(
        contato["nome"],contato['empresa'],contato['email'],contato["telefone"])
    cur.execute(query)
    con.commit()
    return jsonify(contato["nome"] + ' inserido com sucesso'), 200

@app.route('/contato/<string:name>/<int:parcial>', methods=['GET'])
def get_contact_by_name(name,parcial):
    con = sqlite3.connect("agenda.db")
    cur = con.cursor()
    if(parcial == 1):
        query = ("select * from contatos where nome LIKE '%{}%'").format(name)
    else:
        query = ("select * from contatos where nome = '{}'").format(name)
    res = cur.execute(query)
    con.commit()
    return jsonify(res.fetchall()), 200

@app.route('/contato/<string:email>/<int:parcial>', methods=['GET'])
def get_contact_by_mail(email,parcial):
    con = sqlite3.connect("agenda.db")
    cur = con.cursor()
    if(parcial == 1):
        query = ("select * from contatos where email LIKE '%{}%'").format(email)
    else:
        query = ("select * from contatos where email = '{}'").format(email)
    res = cur.execute(query)
    con.commit()
    return jsonify(res.fetchall()), 200

@app.route('/contato/<string:company>/<int:parcial>', methods=['GET'])
def get_contact_by_company(company,parcial):
    con = sqlite3.connect("agenda.db")
    cur = con.cursor()
    if(parcial == 1):
        query = ("select * from contatos where company LIKE '%{}%'").format(company)
    else:
        query = ("select * from contatos where company = '{}'").format(company)
    res = cur.execute(query)
    con.commit()
    return jsonify(res.fetchall()), 200

@app.route('/contato', methods=['PUT'])
def update_contact():
    con = sqlite3.connect("agenda.db")
    cur = con.cursor()
    contato = request.get_json()
    query = ("update contatos set nome = '{0}',empresa = '{1}',email = '{2}',telefone = '{3}' where id = '{4}'").format(
        contato["nome"],contato['empresa'],contato['email'],contato["telefone"],contato['id'])
    cur.execute(query)
    con.commit()
    return jsonify(contato["nome"] + ' atualizado com sucesso'), 200

@app.route('/contato/<int:id>', methods=['DELETE'])
def delete_contact(id):
    con = sqlite3.connect("agenda.db")
    cur = con.cursor()
    contato = request.get_json()
    query = ("delete from contatos where id = '{}'").format(id)
    cur.execute(query)
    con.commit()
    return jsonify('Deletado com sucesso'), 200


if __name__ == '__main__' :
    app.run(debug=True)


