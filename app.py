from flask import Flask, jsonify
import random
#jsonify transforma a resposta em json


app = Flask(__name__)

charadas = [
    {"id": 1, "pergunta": "O que é, o que é? Quanto mais se tira, maior fica?", "resposta": "Buraco"},
    {"id": 2, "pergunta": "O que é, o que é? Tem bico, mas não bica; tem asa, mas não voa?", "resposta": "Bule"},
    {"id": 3, "pergunta": "O que é, o que é? Cai em pé e corre deitado?", "resposta": "Chuva"},
    {"id": 4, "pergunta": "O que é, o que é? Quanto mais quente, mais fresco?", "resposta": "Pão"},
    {"id": 5, "pergunta": "O que é, o que é? Anda com os pés na cabeça?", "resposta": "Piolho"},
    {"id": 6, "pergunta": "O que é, o que é? Tem dentes, mas não morde?", "resposta": "Pente"},
    {"id": 7, "pergunta": "O que é, o que é? Quanto mais se seca, mais molhado fica?", "resposta": "Toalha"},
    {"id": 8, "pergunta": "O que é, o que é? Vive no mar e no banco?", "resposta": "Peixe-espada"},
    {"id": 9, "pergunta": "O que é, o que é? Tem pescoço, mas não tem cabeça?", "resposta": "Garrafa"},
    {"id": 10, "pergunta": "O que é, o que é? Tem olho, mas não vê?", "resposta": "Agulha"}
]

aleatoria = random.randint(1,10)

@app.route('/')
def index():
    return 'API tá on papai 😎'

@app.route('/charadas', methods=['GET'])
def charada():
    return jsonify(charadas), 200 #retorna as charadas em um json no status 200

@app.route('/charadas/id/<int:id>')
def busca(id):
    for charada in charadas:
        if charada['id'] == id:
            return jsonify(charada), 200
    else:
        return jsonify({'mensagem':'ERRO! usuário não encontrado'}), 404

@app.route('/charadas/id/aleatoria', methods=['GET'])
def aleatoria1():
    for charada in charadas:
        if charada['id'] == aleatoria:
            return jsonify(charada), 200
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)