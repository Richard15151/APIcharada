from flask import Flask, jsonify, request
import random
from flask_cors import CORS
import firebase_admin
from firebase_admin import credentials, firestore
import os
import json
from dotenv import load_dotenv

app = Flask(__name__)

CORS(app) ##Trabalha com políticas de segurança
load_dotenv()

FB = json.loads(os.getenv('CONFIG_FIREBASE'))
cred = credentials.Certificate(FB)

firebase_admin.initialize_app(cred)

# conectando com a firestore da firebase
db = firestore.client()

aleatoria = random.randint(1,10)

# ------ROTA PRINCIPAL DE TESTE--------
@app.route('/', methods=['GET'])
def index():
    return 'API tá on papai 😎'

# --------MÉTODO GET - CHARADA ALEATÓRIA----------
@app.route('/charadas', methods=['GET'])
def charada():
    charadas = []
    lista = db.collection('charadas').stream()
    for item in lista:
        charadas.append(item.to_dict())

    if charadas:
        return jsonify(random.choice(charadas)), 200
    else:
        return jsonify({'mensagem':'ERRO, nenhuma charada encontrada'}), 404

#------BUSCAR CHARADA POR ID----------
@app.route('/charadas/id/<id>', methods=['GET'])
def busca(id):
    doc_ref = db.collection('charadas').document(id) #aponta para o documento que você irá usar, sabe o endereço da sua casa, mas não sabe o que está dentro
    doc = doc_ref.get().to_dict() #pega a charada que você quer, entra na casa com o endereço
    if doc:
        return jsonify(doc), 200
    else:
        return jsonify({'mensagem':'Charada não encontrada'})
    
#----------ROTA DE POST - ADICIONAR CHARADA--------
@app.route('/charadas', methods=['POST'])
def adicionar_charada():
    dados = request.json
    if "pergunta" not in dados or "resposta" not in dados:
        return jsonify({'mensagem':'Erro, campos pergunta e resposta são obrigatórios'}), 400
    #Contador
    contador_ref = db.collection('controle_id').document('contador')
    contador_doc = contador_ref.get().to_dict()
    ultimo_id = contador_doc.get('id')
    novo_id = int(ultimo_id) + 1
    contador_ref.update({'id': novo_id}) #atualização da coleção

    db.collection('charadas').document(str(novo_id)).set({
        "id" : novo_id,
        "pergunta": dados['pergunta'],
        "resposta": dados['resposta']
    })
    return jsonify({'Mensagem':'Charada cadastrada com sucesso'})
#------ MÉTODO PUT - ALTERAR CHARADA -----
@app.route('/charadas/<id>', methods=['PUT'])
def alterar_charada(id):
    dados = request.json

    if "pergunta" not in dados or "resposta" not in dados:
        return jsonify({'mensagem':'Erro. Campos pergunta e resposta são obrigatórios'}), 400
    
    doc_ref = db.collection('charadas').document(id)
    doc = doc_ref.get()

    if doc.exists:
        doc_ref.update({
            'pergunta': dados['pergunta'],
            'resposta': dados['resposta']
        })
        return jsonify({'mensagem':'Charada atualizada com sucesso!'}), 201
    else:
        return jsonify({'mensagem':'Erro. Charada não encontrada!'}), 404

#------- MÉTODO DELETE - EXCLUIR CHARADA -----
@app.route('/charadas/<id>', methods=['DELETE'])
def excluir_charada(id):
    doc_ref = db.collection('charadas').document(id)
    doc = doc_ref.get()

    if not doc.exists:
        return jsonify({'mensagem':'Erro. Charada não encontrada'}), 404

    doc_ref.delete()
    return jsonify({'mensagem':'Charada excluída com sucesso!'}), 200
    
if __name__ == '__main__':
    app.run(debug=True)