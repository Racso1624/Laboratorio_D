from token_definition import *
from scanner_simulator import *

class AFD(object):
    def __init__(self):
        self.regex = ['(', '(', 32, '|', 9, '|', 10, ')', '+', ')', '#ws', '|', 105, 102, '#if', '|', '(', '(', 65, '|', 66, '|', 67, '|', 68, '|', 69, '|', 70, '|', 71, '|', 72, '|', 73, '|', 74, '|', 75, '|', 76, '|', 77, '|', 78, '|', 79, '|', 80, '|', 81, '|', 82, '|', 83, '|', 84, '|', 85, '|', 86, '|', 87, '|', 88, '|', 89, '|', 90, '|', 97, '|', 98, '|', 99, '|', 100, '|', 101, '|', 102, '|', 103, '|', 104, '|', 105, '|', 106, '|', 107, '|', 108, '|', 109, '|', 110, '|', 111, '|', 112, '|', 113, '|', 114, '|', 115, '|', 116, '|', 117, '|', 118, '|', 119, '|', 120, '|', 121, '|', 122, ')', '(', '(', 65, '|', 66, '|', 67, '|', 68, '|', 69, '|', 70, '|', 71, '|', 72, '|', 73, '|', 74, '|', 75, '|', 76, '|', 77, '|', 78, '|', 79, '|', 80, '|', 81, '|', 82, '|', 83, '|', 84, '|', 85, '|', 86, '|', 87, '|', 88, '|', 89, '|', 90, '|', 97, '|', 98, '|', 99, '|', 100, '|', 101, '|', 102, '|', 103, '|', 104, '|', 105, '|', 106, '|', 107, '|', 108, '|', 109, '|', 110, '|', 111, '|', 112, '|', 113, '|', 114, '|', 115, '|', 116, '|', 117, '|', 118, '|', 119, '|', 120, '|', 121, '|', 122, ')', '|', '(', '(', '_', ')', '*', ')', '|', '(', 48, '|', 49, '|', 50, '|', 51, '|', 52, '|', 53, '|', 54, '|', 55, '|', 56, '|', 57, ')', ')', '*', ')', '#id', '|', '(', '(', '(', 48, '|', 49, '|', 50, '|', 51, '|', 52, '|', 53, '|', 54, '|', 55, '|', 56, '|', 57, ')', '+', ')', '(', 46, '(', '(', 48, '|', 49, '|', 50, '|', 51, '|', 52, '|', 53, '|', 54, '|', 55, '|', 56, '|', 57, ')', '+', ')', ')', '?', '(', 69, '(', 43, '|', 45, ')', '?', '(', '(', 48, '|', 49, '|', 50, '|', 51, '|', 52, '|', 53, '|', 54, '|', 55, '|', 56, '|', 57, ')', '+', ')', ')', '?', ')', '#number', '|', 59, '#;', '|', 58, 61, '#:=', '|', 60, '#<', '|', 61, '#=', '|', 43, '#+', '|', 45, '#-', '|', 42, '#*', '|', 47, '#/', '|', 40, '#(', '|', 41, '#)']
        self.states = ['S0', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7', 'S8', 'S9', 'S10', 'S11', 'S12', 'S13', 'S14', 'S15', 'S16', 'S17', 'S18', 'S19', 'S20', 'S21']
        self.transitions = [['S0', 32, 'S1'], ['S0', 9, 'S1'], ['S0', 10, 'S1'], ['S0', 105, 'S2'], ['S0', 102, 'S3'], ['S0', 65, 'S3'], ['S0', 66, 'S3'], ['S0', 67, 'S3'], ['S0', 68, 'S3'], ['S0', 69, 'S3'], ['S0', 70, 'S3'], ['S0', 71, 'S3'], ['S0', 72, 'S3'], ['S0', 73, 'S3'], ['S0', 74, 'S3'], ['S0', 75, 'S3'], ['S0', 76, 'S3'], ['S0', 77, 'S3'], ['S0', 78, 'S3'], ['S0', 79, 'S3'], ['S0', 80, 'S3'], ['S0', 81, 'S3'], ['S0', 82, 'S3'], ['S0', 83, 'S3'], ['S0', 84, 'S3'], ['S0', 85, 'S3'], ['S0', 86, 'S3'], ['S0', 87, 'S3'], ['S0', 88, 'S3'], ['S0', 89, 'S3'], ['S0', 90, 'S3'], ['S0', 97, 'S3'], ['S0', 98, 'S3'], ['S0', 99, 'S3'], ['S0', 100, 'S3'], ['S0', 101, 'S3'], ['S0', 103, 'S3'], ['S0', 104, 'S3'], ['S0', 106, 'S3'], ['S0', 107, 'S3'], ['S0', 108, 'S3'], ['S0', 109, 'S3'], ['S0', 110, 'S3'], ['S0', 111, 'S3'], ['S0', 112, 'S3'], ['S0', 113, 'S3'], ['S0', 114, 'S3'], ['S0', 115, 'S3'], ['S0', 116, 'S3'], ['S0', 117, 'S3'], ['S0', 118, 'S3'], ['S0', 119, 'S3'], ['S0', 120, 'S3'], ['S0', 121, 'S3'], ['S0', 122, 'S3'], ['S0', 48, 'S4'], ['S0', 49, 'S4'], ['S0', 50, 'S4'], ['S0', 51, 'S4'], ['S0', 52, 'S4'], ['S0', 53, 'S4'], ['S0', 54, 'S4'], ['S0', 55, 'S4'], ['S0', 56, 'S4'], ['S0', 57, 'S4'], ['S0', 43, 'S5'], ['S0', 45, 'S6'], ['S0', 59, 'S7'], ['S0', 58, 'S8'], ['S0', 61, 'S9'], ['S0', 60, 'S10'], ['S0', 42, 'S11'], ['S0', 47, 'S12'], ['S0', 40, 'S13'], ['S0', 41, 'S14'], ['S1', 32, 'S1'], ['S1', 9, 'S1'], ['S1', 10, 'S1'], ['S2', 105, 'S3'], ['S2', 102, 'S15'], ['S2', 65, 'S3'], ['S2', 66, 'S3'], ['S2', 67, 'S3'], ['S2', 68, 'S3'], ['S2', 69, 'S3'], ['S2', 70, 'S3'], ['S2', 71, 'S3'], ['S2', 72, 'S3'], ['S2', 73, 'S3'], ['S2', 74, 'S3'], ['S2', 75, 'S3'], ['S2', 76, 'S3'], ['S2', 77, 'S3'], ['S2', 78, 'S3'], ['S2', 79, 'S3'], ['S2', 80, 'S3'], ['S2', 81, 'S3'], ['S2', 82, 'S3'], ['S2', 83, 'S3'], ['S2', 84, 'S3'], ['S2', 85, 'S3'], ['S2', 86, 'S3'], ['S2', 87, 'S3'], ['S2', 88, 'S3'], ['S2', 89, 'S3'], ['S2', 90, 'S3'], ['S2', 97, 'S3'], ['S2', 98, 'S3'], ['S2', 99, 'S3'], ['S2', 100, 'S3'], ['S2', 101, 'S3'], ['S2', 103, 'S3'], ['S2', 104, 'S3'], ['S2', 106, 'S3'], ['S2', 107, 'S3'], ['S2', 108, 'S3'], ['S2', 109, 'S3'], ['S2', 110, 'S3'], ['S2', 111, 'S3'], ['S2', 112, 'S3'], ['S2', 113, 'S3'], ['S2', 114, 'S3'], ['S2', 115, 'S3'], ['S2', 116, 'S3'], ['S2', 117, 'S3'], ['S2', 118, 'S3'], ['S2', 119, 'S3'], ['S2', 120, 'S3'], ['S2', 121, 'S3'], ['S2', 122, 'S3'], ['S2', '_', 'S3'], ['S2', 48, 'S3'], ['S2', 49, 'S3'], ['S2', 50, 'S3'], ['S2', 51, 'S3'], ['S2', 52, 'S3'], ['S2', 53, 'S3'], ['S2', 54, 'S3'], ['S2', 55, 'S3'], ['S2', 56, 'S3'], ['S2', 57, 'S3'], ['S3', 105, 'S3'], ['S3', 102, 'S3'], ['S3', 65, 'S3'], ['S3', 66, 'S3'], ['S3', 67, 'S3'], ['S3', 68, 'S3'], ['S3', 69, 'S3'], ['S3', 70, 'S3'], ['S3', 71, 'S3'], ['S3', 72, 'S3'], ['S3', 73, 'S3'], ['S3', 74, 'S3'], ['S3', 75, 'S3'], ['S3', 76, 'S3'], ['S3', 77, 'S3'], ['S3', 78, 'S3'], ['S3', 79, 'S3'], ['S3', 80, 'S3'], ['S3', 81, 'S3'], ['S3', 82, 'S3'], ['S3', 83, 'S3'], ['S3', 84, 'S3'], ['S3', 85, 'S3'], ['S3', 86, 'S3'], ['S3', 87, 'S3'], ['S3', 88, 'S3'], ['S3', 89, 'S3'], ['S3', 90, 'S3'], ['S3', 97, 'S3'], ['S3', 98, 'S3'], ['S3', 99, 'S3'], ['S3', 100, 'S3'], ['S3', 101, 'S3'], ['S3', 103, 'S3'], ['S3', 104, 'S3'], ['S3', 106, 'S3'], ['S3', 107, 'S3'], ['S3', 108, 'S3'], ['S3', 109, 'S3'], ['S3', 110, 'S3'], ['S3', 111, 'S3'], ['S3', 112, 'S3'], ['S3', 113, 'S3'], ['S3', 114, 'S3'], ['S3', 115, 'S3'], ['S3', 116, 'S3'], ['S3', 117, 'S3'], ['S3', 118, 'S3'], ['S3', 119, 'S3'], ['S3', 120, 'S3'], ['S3', 121, 'S3'], ['S3', 122, 'S3'], ['S3', '_', 'S3'], ['S3', 48, 'S3'], ['S3', 49, 'S3'], ['S3', 50, 'S3'], ['S3', 51, 'S3'], ['S3', 52, 'S3'], ['S3', 53, 'S3'], ['S3', 54, 'S3'], ['S3', 55, 'S3'], ['S3', 56, 'S3'], ['S3', 57, 'S3'], ['S4', 69, 'S16'], ['S4', 48, 'S4'], ['S4', 49, 'S4'], ['S4', 50, 'S4'], ['S4', 51, 'S4'], ['S4', 52, 'S4'], ['S4', 53, 'S4'], ['S4', 54, 'S4'], ['S4', 55, 'S4'], ['S4', 56, 'S4'], ['S4', 57, 'S4'], ['S4', 46, 'S17'], ['S8', 61, 'S18'], ['S15', 105, 'S3'], ['S15', 102, 'S3'], ['S15', 65, 'S3'], ['S15', 66, 'S3'], ['S15', 67, 'S3'], ['S15', 68, 'S3'], ['S15', 69, 'S3'], ['S15', 70, 'S3'], ['S15', 71, 'S3'], ['S15', 72, 'S3'], ['S15', 73, 'S3'], ['S15', 74, 'S3'], ['S15', 75, 'S3'], ['S15', 76, 'S3'], ['S15', 77, 'S3'], ['S15', 78, 'S3'], ['S15', 79, 'S3'], ['S15', 80, 'S3'], ['S15', 81, 'S3'], ['S15', 82, 'S3'], ['S15', 83, 'S3'], ['S15', 84, 'S3'], ['S15', 85, 'S3'], ['S15', 86, 'S3'], ['S15', 87, 'S3'], ['S15', 88, 'S3'], ['S15', 89, 'S3'], ['S15', 90, 'S3'], ['S15', 97, 'S3'], ['S15', 98, 'S3'], ['S15', 99, 'S3'], ['S15', 100, 'S3'], ['S15', 101, 'S3'], ['S15', 103, 'S3'], ['S15', 104, 'S3'], ['S15', 106, 'S3'], ['S15', 107, 'S3'], ['S15', 108, 'S3'], ['S15', 109, 'S3'], ['S15', 110, 'S3'], ['S15', 111, 'S3'], ['S15', 112, 'S3'], ['S15', 113, 'S3'], ['S15', 114, 'S3'], ['S15', 115, 'S3'], ['S15', 116, 'S3'], ['S15', 117, 'S3'], ['S15', 118, 'S3'], ['S15', 119, 'S3'], ['S15', 120, 'S3'], ['S15', 121, 'S3'], ['S15', 122, 'S3'], ['S15', '_', 'S3'], ['S15', 48, 'S3'], ['S15', 49, 'S3'], ['S15', 50, 'S3'], ['S15', 51, 'S3'], ['S15', 52, 'S3'], ['S15', 53, 'S3'], ['S15', 54, 'S3'], ['S15', 55, 'S3'], ['S15', 56, 'S3'], ['S15', 57, 'S3'], ['S16', 48, 'S19'], ['S16', 49, 'S19'], ['S16', 50, 'S19'], ['S16', 51, 'S19'], ['S16', 52, 'S19'], ['S16', 53, 'S19'], ['S16', 54, 'S19'], ['S16', 55, 'S19'], ['S16', 56, 'S19'], ['S16', 57, 'S19'], ['S16', 43, 'S20'], ['S16', 45, 'S20'], ['S17', 48, 'S21'], ['S17', 49, 'S21'], ['S17', 50, 'S21'], ['S17', 51, 'S21'], ['S17', 52, 'S21'], ['S17', 53, 'S21'], ['S17', 54, 'S21'], ['S17', 55, 'S21'], ['S17', 56, 'S21'], ['S17', 57, 'S21'], ['S19', 48, 'S19'], ['S19', 49, 'S19'], ['S19', 50, 'S19'], ['S19', 51, 'S19'], ['S19', 52, 'S19'], ['S19', 53, 'S19'], ['S19', 54, 'S19'], ['S19', 55, 'S19'], ['S19', 56, 'S19'], ['S19', 57, 'S19'], ['S20', 48, 'S19'], ['S20', 49, 'S19'], ['S20', 50, 'S19'], ['S20', 51, 'S19'], ['S20', 52, 'S19'], ['S20', 53, 'S19'], ['S20', 54, 'S19'], ['S20', 55, 'S19'], ['S20', 56, 'S19'], ['S20', 57, 'S19'], ['S21', 69, 'S16'], ['S21', 48, 'S21'], ['S21', 49, 'S21'], ['S21', 50, 'S21'], ['S21', 51, 'S21'], ['S21', 52, 'S21'], ['S21', 53, 'S21'], ['S21', 54, 'S21'], ['S21', 55, 'S21'], ['S21', 56, 'S21'], ['S21', 57, 'S21']]
        self.initial_state = 'S0'
        self.final_states = {'S1': '#ws', 'S2': '#id', 'S3': '#id', 'S4': '#number', 'S5': '#+', 'S6': '#-', 'S7': '#;', 'S9': '#=', 'S10': '#<', 'S11': '#*', 'S12': '#/', 'S13': '#(', 'S14': '#)', 'S15': '#if', 'S18': '#:=', 'S19': '#number', 'S21': '#number'}
        self.symbols = [32, 9, 10, '#ws', 105, 102, '#if', 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 97, 98, 99, 100, 101, 103, 104, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, '_', 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, '#id', 46, 43, 45, '#number', 59, '#;', 58, 61, '#:=', 60, '#<', '#=', '#+', '#-', 42, '#*', 47, '#/', 40, '#(', 41, '#)']

def tokenScanner(token):
	if(token == '#ws'):
		return WHITESPACE
	if(token == '#if'):
		return IF
	if(token == '#id'):
		return ID
	if(token == '#number'):
		return NUMBER
	if(token == '#;'):
		return SEMICOLON
	if(token == '#:='):
		return ASSIGNOP
	if(token == '#<'):
		return LT
	if(token == '#='):
		return EQ
	if(token == '#+'):
		return PLUS
	if(token == '#-'):
		return MINUS
	if(token == '#*'):
		return TIMES
	if(token == '#/'):
		return DIV
	if(token == '#('):
		return LPAREN
	if(token == '#)'):
		return RPAREN

	return ERROR

afd = AFD()
simulation('./tests/token_test.txt', tokenScanner, afd)