from webbrowser import BackgroundBrowser
from flask import Flask

app = Flask(__name__)

# criar a 1ª página do site
# route -> nomedomeusite.com/contatos
# função -> o que você quer exibir naquela página
# template

@app.route("/")
def homepage():
    return "<h1>Esse é o meu primeiro site em Flask! </h1>"

@app.route("/contatos")
def contatos():
    return "<div style = background-color: red;><h1>Entre em contato através:</h1> <p><h3>E-mail:</h3> duartecostap@gmail.com</p> <p><h3>Telefone:</h3> (11) 9876-5493</p></div>"

# colocar site no ar
if __name__ == "__main__":
    app.run(debug=True)