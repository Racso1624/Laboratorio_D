class ScannerProducer(object):
    def __init__(self, afd, name, tokens):
        self.afd = afd
        self.name = name
        self.tokens = tokens
        self.scannerConstructor()
        
    
    def scannerConstructor(self):
        file = open(f"./scanners/{self.name}.py", "w")  
        file.write("from token_definition import *\n")
        file.write("from scanner_simulator import *\n\n")
        file.write("class AFD(object):\n")
        file.write("    def __init__(self):\n")
        file.write(f"        self.regex = {self.afd.regex}\n")
        file.write(f"        self.states = {self.afd.states}\n")
        file.write(f"        self.transitions = {self.afd.transitions}\n")
        file.write(f"        self.initial_state = '{self.afd.initial_state}'\n")
        file.write(f"        self.final_state = {self.afd.final_states}\n")
        file.write(f"        self.symbols = {self.afd.symbols}\n\n")
        file.write("def tokenScanner(token):\n")
        for i in self.tokens:
            file.write(f"\tif(token == '{i}'):\n")
            file.write(f"\t\t{self.tokens[i]}\n")
        file.write(f"\n\treturn ERROR\n\n")
        file.write("afd = AFD()\n")
        file.write("simulation('token_test.txt', tokenScanner(), afd)")
        file.close()