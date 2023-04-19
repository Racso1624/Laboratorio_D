# Oscar Fernando López Barrios
# Carné 20679

# Clase de Regex
class Regex (object):

    # Se inicia la funcion
    def __init__(self, regex):
        self.expression = regex
        self.operators = []
        self.errorValidation()
        self.postfix_expression = self.postfixConversion() 

    # Se realiza para brindar el resultado de la expresion postfix
    def __repr__(self) -> str:
        return self.postfix_expression
    
    # Se ven la validacion de los errores
    def errorValidation(self):
        expression = self.expression
        if(expression.count('(') != expression.count(')')):
            raise Exception("ERROR: Cantidad de Parentesis Incorrecta")
        if(expression[0] in ".|*+?"):
            raise Exception("ERROR: No se puede iniciar con simbolo de operacion")
        
        # for i in range(len(expression)):
        #     if(isinstance(expression[i], str) and expression[i] in ".|*+?" and expression[i + 1] in ".|*+?"):
        #         raise Exception("ERROR: No se pueden tener dos operadores juntos en una expresion")

    # Funcion para conocer la precedencia
    def operatorPrecedence(self, character):

        # Se realiza un diccionario con precedencia
        precedence = {'(' : 1, '|' : 2, '.' : 3, '?' : 4, '*' : 4, '+' : 4}

        # Se devuelve la precedencia segun el caracter ingresado
        try:
            return precedence[character]
        except:
            return 5

    # Algoritmo implementando Shunting-Yard
    def postfixConversion(self):
        
        # Se crean la lista de operadores y caracteres
        # Ademas se crea la expresion
        operators_list = ['|', '?', '*', '+']
        characters_queue = []
        postfix_expression = []

        # Se itera sobre la expresion para crear la cola de caracteres a utilizar para el algoritmo
        # Ademas se agregan los '.' para la concatenacion que se realizara
        for i in range(len(self.expression)):
            char = self.expression[i]

            if((i + 1) < len(self.expression)):
                next_char = self.expression[i + 1]
                characters_queue.append(char)

                if((char != '(') and (next_char != ')') and (next_char not in operators_list) and (char != '|')):
                    characters_queue.append('.')
        
        characters_queue.append(self.expression[len(self.expression) - 1])

        # Se itera en los caracteres para obtener la precedencia
        for char in characters_queue:

            if(char == '('):
                self.operators.append(char)
            elif(char == ')'):
                while(self.operators[-1] != '('):
                    postfix_expression.append(self.operators.pop())
                self.operators.pop()
            else:
                while(len(self.operators) > 0):
                    last_char = self.operators[-1]
                    last_char_precedence = self.operatorPrecedence(last_char)
                    char_precedence = self.operatorPrecedence(char)

                    if(last_char_precedence >= char_precedence):
                        postfix_expression.append(self.operators.pop())
                    else:
                        break
                
                self.operators.append(char)

        while(len(self.operators) > 0):
            postfix_expression.append(self.operators.pop())
        return postfix_expression