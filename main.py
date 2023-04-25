# Oscar Fernando López Barrios
# Carné 20679

# Se importan librerias
from filereader import *
from syntaxtree import *
from afd_construction import *
from scanner_producer import *

# Se toma el filename
filename = "./tests/slr-1.yal"
# Se obtiene el filereader
file_reader = File(filename)
# Se obtiene la regex
regex = file_reader.regex
tokens = file_reader.tokens_list
print(regex)
print(tokens)
# Se crea el AFD
afd = afdConstruction(regex, "Yalex 1")
afd.simulation("./tests/token_test.txt")
ScannerProducer(afd, "Yalex_1", tokens)