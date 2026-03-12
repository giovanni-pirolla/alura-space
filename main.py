import sys
import os
print(f"Executável: {sys.executable}")
print(f"Caminhos de busca: {sys.path}")
try:
    import dotenv
    print("Dotenv encontrado em:", dotenv.__file__)
except ImportError:
    print("Erro: Módulo não encontrado no sys.path")