from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DbConnectionHandler:
    def __init__(self):
        # Define a string de conexão com o banco de dados SQLite
        self.__conenection_string = "sqlite:///schema.db"

        # Cria o motor de conexão com o banco usando SQLAlchemy
        self.__engine = self.__create_database_engine()

        # Inicializa a variável de sessão como None (será criada depois)
        self.session = None

    # Método privado para criar o motor de conexão com o banco
    def __create_database_engine(self):
        # Usa a string de conexão para instanciar o motor
        engine = create_engine(self.__conenection_string)
        return engine

    # Método chamado automaticamente ao entrar no bloco 'with'
    def __enter__(self):
        # Cria uma fábrica de sessões vinculada ao motor de conexão
        session_make = sessionmaker(bind=self.__engine)

        # Instancia uma sessão a partir da fábrica
        self.session = session_make()
        return self

    # Método chamado automaticamente ao sair do bloco 'with'
    def __exit__(self, exc_type, exc_val, exc_tb):
        # Encerra a sessão para liberar recursos
        self.session.close()
