class MinhaClasse:
    # executa quando inicia o codigo
    def __enter__(self):
        print("Entrei")
        
    # executa quando acaba o codigo
    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Estou no exit")

# executa no meio do codigo
with MinhaClasse() as mc:
    print("Entrei no with")