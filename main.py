from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

# Função para gerar a senha
def gerar_senha(comprimento):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(comprimento))
    return senha

# Rota principal
@app.route('/', methods=['GET', 'POST'])
def home():
    senha_gerada = None
    if request.method == 'POST':
        tamanho = int(request.form['tamanho'])
        acao = (request.form['acao'])
        if acao =="gerar":
            senha_gerada = gerar_senha(tamanho)
        elif acao == "limpar":
            senha_gerada = None
    return render_template('home.html', senha=senha_gerada)


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)


@app.route('/delete', methods=['DELETE'])
def delete():
    
    return {"mensagem": "Senha removida com sucesso"}, 200

