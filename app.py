from flask import Flask, render_template

#pagina para cadastrar cliente
#pagina para mostrar todos os clientes
#pagina para conversar com cliente especifico 

#redirect para uma pagina certa caso o cara for para uma pagina errada

app =  Flask(__name__)

@app.route('/clientes')
def mostrar_clientes():
    return 'todos clientes'

@app.route('/cadastro')
def cadastrar_cliente():
    return render_template('cadastro.html')

@app.route('/chat')
def conversar_cliente_especifico():
    return 'conversa com cliente especifico'


if __name__ == "__main__" :
    app.run(debug=True)