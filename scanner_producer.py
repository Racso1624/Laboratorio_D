class ScannerProducer(object):
    def __init__(self, afd, name):
        self.afd = afd
        self.name = name
        self.scannerConstructor()
        
    
    def scannerConstructor(self):
        file = open(f"./scanners/{self.name}.py", "w")
        file.write("class AFD(object):\n")
        file.write("    def __init__(self):\n")
        file.write(f"        self.regex = {self.afd.regex}\n")
        file.write(f"        self.states = {self.afd.states}\n")
        file.write(f"        self.transitions = {self.afd.transitions}\n")
        file.write(f"        self.initial_state = '{self.afd.initial_state}'\n")
        file.write(f"        self.final_state = {self.afd.final_state}\n")
        file.write(f"        self.symbols = {self.afd.symbols}\n")
        file.close()