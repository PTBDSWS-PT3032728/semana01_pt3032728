# A very simple Flask Hello World app for you to get started with...
from flask import Flask, request, make_response, redirect, abort
app = Flask(__name__)

#Tela inicial com uma função simples que retorna um "Hello World".
@app.route('/') #Rota padrão do site (inicial)
def hello_world(): #Função
    return '<h1>Hello World!</h1><p><b><h2>Disciplina PTBDSWS</h2></b></p>' #Retorno em string, utilizando tags

#Ao utilizar a url para adicionar o nome do usuário, é possível utilizá-lo como atributo para passar como parâmetro de uma função que retorna esse nome dentro do site.
@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, {}!</h1>'.format(name)

#O request serve para coletar dados que o servidor recebe do usuário, no caso o User-Agent apresenta os dados do navegador e o sistema operacional utilizado.
@app.route('/contextorequisicao')
def dadosNavegador():
    return 'Your browser is {}'.format(request.headers.get('User-Agent'))

#O erro de Bad Request acontece quando o servidor recebe uma requisição com informações faltantes ou erradas pelo lado do cliente, e não consegue interpretar.
#Obs: No exemplo da atividade aparenta ser um retorno simples escrito. Mas poderia ser utilizado o abort(400). Na dúvida, deixei conforme aparenta o mais próximo da resolução.
@app.route('/codigostatusdiferente', methods=['POST'])  #Simulei que essa rota recebia o método POST
def codigoStatusDiferente():
    nome = request.form.get('nome') #Por meio de request o valor de 'nome' é coletado (se foi enviado)
    if not nome: #Se 'nome' não teve nenhum valor enviado, retorna bad request
        return 'Bad request', 400 #Como no caso não foi, o servidor retorna o erro 400.
    else: #Se teve um valor em 'nome', retorna Ok
        return 'Ok, {}.'.format(nome)

#É possível criar objetos de resposta, que podem carregar atributos e serem retornados
@app.route('/objetoresposta')
def objetoResposta():
    resposta = make_response('<h1>This document carries a cookie!</h1>') #Objeto de resposta criado, nesse caso, uma string
    resposta.set_cookie('resposta', '42') #Atribuí um cookie a esse objeto de resposta(Esse cookie pode ser verificado utilizando o inspecionar)
    return resposta

#É possível redirecionar o cliente para uma página externa por meio do redirect(url externa), da classe redirect.
@app.route('/redirecionamento')
def redirecionar():
    return redirect('https://ptb.ifsp.edu.br/')

#abortar se trata da função abort() que tem o objetivo de interromper um processo e indicar um status de erro como retorno.
@app.route('/abortar')
def abortar():
    abort(404)