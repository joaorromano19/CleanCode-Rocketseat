import pytest
from src.models.connection.db_connection_handler import DbConnectionHandler

@pytest.mark.skip(reason="Integration with DB")
def teste_db_connection_handler():
    db_conn_handler = DbConnectionHandler()

    assert db_conn_handler.session is None
    
    with db_conn_handler:
        print(db_conn_handler.session)
        assert db_conn_handler.session is not None