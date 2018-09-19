import os, sys

class Parser:
    def __init__(self, infile):
        with open(infile + ".vm", 'r') as file:
            self.lines = file.readlines()
        self.command = ["","",0]
        self.aux = ""
        self.aux2 = ""
        self.aux3 = 0
        self.currentLine = 0
        self.commands_dict = {
            'add': 'C_ARITHMETIC','sub': 'C_ARITHMETIC', 'neg': 'C_ARITHMETIC', 'eq': 'C_ARITHMETIC', 
            'gt': 'C_ARITHMETIC', 'lt': 'C_ARITHMETIC', 'and': 'C_ARITHMETIC',
            'or': 'C_ARITHMETIC', 'not': 'C_ARITHMETIC', 'push': 'C_PUSH', 'pop': 'C_POP'}

    #Verificar si hay o no mas comandos para traduccir.
    def hasMoreCommands(self):
        if self.currentLine <= (len(self.lines) - 1):
            return True
        else:
            return False
    #Avanzar de una linea a otra.
    def advance(self):
        self.currentLine+=1
        line = self.lines[self.currentLine-1]
        if self.hasMoreCommands:
            if not line.startswith('//'):
                self.command = line.split()
                for x in self.command:
                    self.aux = self.command[0]
                        
    #Ver que tipo de comando es el que ingresamos, de no estar decimos que probablemente no esta implementado.
    def command_type(self):
        return self.commands_dict.get(self.command[0], "// No ha sido implementado.")

    #Sacar la segunda parte del comando.
    def arg1(self):
        return self.command[1]

    #Sacar el index del comando.
    def arg2(self):
        return self.command[2]    


