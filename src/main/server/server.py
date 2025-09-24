from flask import Flask
from src.main.routes.users_route import user_routes_bp

# Cria uma instância da aplicação Flask
# '__name__' é usado para que o Flask saiba onde está o ponto de entrada da aplicação
app = Flask(__name__)

# Registra o blueprint 'user_routes_bp' na aplicação principal
# Isso permite que as rotas definidas no blueprint sejam integradas ao app
app.register_blueprint(user_routes_bp)