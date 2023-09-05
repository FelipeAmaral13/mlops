from flask import Flask
from flask_basicauth import BasicAuth
import os

app = Flask(__name__)

# Configurando as credenciais de autenticação
app.config['BASIC_AUTH_USERNAME'] = os.environ.get('BASIC_AUTH_USERNAME')
app.config['BASIC_AUTH_PASSWORD'] = os.environ.get('BASIC_AUTH_PASSWORD')

# Inicializando a extensão Flask-BasicAuth
basic_auth = BasicAuth(app)

@app.route('/')
def home():
    return 'Bem-vindo à página inicial! Você está autenticado.'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
