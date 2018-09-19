class Parser(object):
	#Definimos los tipos de comandos con estos numeros para darles un valor numerico.
    A_COMMAND = 0
    L_COMMAND = 1
    C_COMMAND = 2
    
		#Constructor.
    def __init__(self, infile):
        with open(infile, 'r') as file:
            self.lines = file.readlines()
        self.currentLine = 0			
        self.command = ''
        
		#Verificamos si hay o no mas lineas en el archivo que leemos. 
    def hasMoreCommands(self):
        if self.currentLine <= (len(self.lines)-1): 
            return True
        else:
            return False
		
    #Primero nos fijamos si hay mas comandos y dependiendo de esto avanzamos o no.
    def advance(self):
        self.currentLine+=1
        line = self.lines[self.currentLine-1]
        if self.hasMoreCommands:
            if not line.startswith('//'):
                a = line.strip()
                if a.find('//') != -1:
                    pos = a.find('//')
                    a = a[0:pos]
                self.command = a
           
    #Verificamos que tipo de comando tenemos en la linea que estamos actualmente.   
    def commandType(self):
        l = len(self.command)
        if self.command.startswith('@'):
          	return self.A_COMMAND
        elif self.command.startswith('(') and self.command.endswith(')'):
          	return self.L_COMMAND
        elif self.command.find('=') != -1 or self.command.find(';') != -1:
          	return self.C_COMMAND
    
    #Retornamos el simbolo dado por el comando de tipo A o tipo L.      
    def symbol(self):
       	a = self.command
        l = len(a)
        if a.startswith('@'):
            b = a[1:l]
            if b.find('//') != -1:
                pos = b.find('//')
                b = b[0:pos]
            #if b.isdigit() == False:
            return b
        elif a.startswith('('):
            b = a[1:l-1] 
            if b.isdigit() == False:
                if b.find('//') != -1:
                    pos = b.find('//')
                    b = b[0:pos]
                return b
        
    #Retornamos la parte del dest de el comando C.
    def dest(self):   
        c = ''
        if '=' in self.command:
            c = self.command[0:self.command.find('=')]
        return c
      
    #Retornamos la parte del comp de el comando C.  
    def comp(self):
        l = len(self.command)
        c = ''
        if '=' in self.command:
            pos = self.command.find('=')
            if ';' in self.command:
                pos2 = self.command.find(';')
                c = self.command[pos+1:pos2]
            else:
          	    c = self.command[pos+1:l+1]
        elif ';' in self.command:				
          pos = self.command.find(';')
          c = self.command[0:pos]
        return c
      
      #Retornamos la parte del jump de el comando C.
    def jump(self):
        l = len(self.command)
        c = ''
        if ';' in self.command:
        	pos = self.command.find(';')
        	c = self.command[pos+1:l+1]
        return c