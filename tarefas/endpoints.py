from flask import jsonify, request
from sqlalchemy import text
from main import app, db

@app.route("/tarefas", methods=["GET"])
def get_tarefas():
    with db.get_engine().connect() as conn:
        rset = list()
        result = conn.execute(text("SELECT id, descricao, quantidade, preco_unitario, compra_realizada FROM itens_compra"))
        for row in result:
            rset.append({"id":row[0], 
                "descricao":row[1],
                "quantidade":row[2],
                "preco_unitario":row[3],
                "compra_realizada":row[4]})

        return jsonify(rset)

@app.route("/tarefas", methods=["POST"])
def post_tarefa():
    print ('post')
    print (request.json)

    return '', 200
