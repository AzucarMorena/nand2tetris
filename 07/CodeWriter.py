import sys
class CodeWriter:
    def __init__(self, outfile):
        self.out = outfile
        self.outfile = open(self.out + ".asm", 'w+')
        self.labels = 1
        self.root = sys.argv[1]

    #Traducir las operaciones aritmeticas a asm.
    def writeAritmethic(self, command):
        trans = ""
        if command == "add":
            trans += "@SP\n" 
            trans += "AM=M-1\n"
            trans += "D=M\n"
            trans += "A=A-1\n" 
            trans += "M=D+M\n" 
        elif command == "sub":
            trans += "@SP\n" 
            trans += "AM=M-1\n"
            trans += "D=M\n"
            trans += "A=A-1\n" 
            trans += "M=D-M\n"
        elif command == "neg":
            trans += "@SP\n" 
            trans += "A=M-1\n" 
            trans += "M=-M\n"
        elif command == "not":
            trans += "@SP\n" 
            trans += "A=M-1\n" 
            trans += "M=!M\n" 
        elif command == "or":
            trans += "@SP\n" 
            trans += "AM=M-1\n"
            trans += "D=M\n" 
            trans += "A=A-1\n"
            trans += "M=D|M\n" 
        elif command == "and":
            trans += "@SP\n" 
            trans += "AM=M-1\n"
            trans += "D=M\n" 
            trans += "A=A-1\n"
            trans += "M=D&M\n"
        elif command == "eq":
            label = str(self.labels)
            self.labels += 1
            trans += "@SP\n" 
            trans += "AM=M-1\n"
            trans += "D=M\n" 
            trans += "@SP\n" 
            trans += "A=A-1\n"
            trans += "D=M-D\n" 
            trans += "M=-1\n" 
            trans += "@eqTrue" + label + "\n"
            trans += "D;JEQ\n"
            trans += "@SP\n" 
            trans += "A=A-1\n"
            trans += "M=0\n" 
            trans += "(eqTrue" + label + ")\n"
        elif command == "gt":
            label = str(self.labels)
            self.labels += 1
            trans += "@SP\n" 
            trans += "AM=M-1\n"
            trans += "D=M\n" 
            trans += "@SP\n" 
            trans += "A=A-1\n"
            trans += "D=M-D\n"
            trans += "M=-1\n" 
            trans += "@gtTrue" + label + "\n" 
            trans += "D;JGT\n"
            trans += "@SP\n" 
            trans += "A=A-1\n"
            trans += "M=0\n" 
            trans += "(gtTrue" + label + ")\n"
        elif command == "lt":
            label = str(self.labels)
            self.labels += 1
            trans += "@SP\n" 
            trans += "AM=M-1\n"
            trans += "D=M\n" 
            trans += "@SP\n" 
            trans += "A=A-1\n"
            trans += "D=M-D\n"
            trans += "M=-1\n" 
            trans += "@ltTrue" + label + "\n"
            trans += "D;JLT\n"
            trans += "@SP\n"
            trans += "A=A-1\n"
            trans += "M=0\n" 
            trans += "(ltTrue" + label + ")\n"
        else:
            trans = str(command)
        self.writen(trans)

    #Traducir las operaciones de push y pop.
    def writePushPop(self, command, segment, index):
        trans = ""
        if command == "push":
            if segment == "constant":
                trans += "@" + index + "\n"
                trans += "D=A\n" 
                trans += "@SP\n" 
                trans += "A=M\n" 
                trans += "M=D\n" 
                trans += "@SP\n" 
                trans += "M=M+1\n" 
            elif segment == "static":
                trans += "@" + str(16+int(index)) + "\n"
                trans += "D=M\n"
                trans += "@SP\n" 
                trans += "A=M\n" 
                trans += "M=D\n"
                trans += "@SP\n"
                trans += "M=M+1\n"
            elif segment == "argument":
                trans += "@" + index + "\n" 
                trans += "D=A\n"
                trans += "@ARG\n"
                trans += "A=D+M\n" 
                trans += "D=M\n"
                trans += "@SP\n" 
                trans += "A=M\n"
                trans += "M=D\n"
                trans += "@SP\n" 
                trans += "M=M+1\n"
            elif segment == "local":
                trans += "@" + index + "\n" 
                trans += "D=A\n"
                trans += "@LCL\n"
                trans += "A=M+D\n" 
                trans += "D=M\n"
                trans += "@SP\n" 
                trans += "A=M\n"
                trans += "M=D\n"
                trans += "@SP\n" 
                trans += "M=M+1\n"
            elif segment == "this":
                trans += "@" + index + "\n" 
                trans += "D=A\n"
                trans += "@THIS\n"
                trans += "A=M+D\n" 
                trans += "D=M\n"
                trans += "@SP\n" 
                trans += "A=M\n"
                trans += "M=D\n"
                trans += "@SP\n" 
                trans += "M=M+1\n"
            elif segment == "that":
                trans += "@" + index + "\n"
                trans += "D=A\n"
                trans += "@THAT\n"
                trans += "A=M+D\n" 
                trans += "D=M\n"
                trans += "@SP\n" 
                trans += "A=M\n"
                trans += "M=D\n"
                trans += "@SP\n" 
                trans += "M=M+1\n"
            elif segment == "temp":
                trans += "@" + index + "\n" 
                trans += "D=A\n"
                trans += "@5\n"
                trans += "A=A+D\n" 
                trans += "D=M\n"
                trans += "@SP\n"
                trans += "A=M\n"
                trans += "M=D\n"
                trans += "@SP\n"
                trans += "M=M+1\n"
            else:
                trans += segment + " //No ha sido implementado aun.\n"
        elif command == "pop":
            if segment == "static":
                trans += "@SP\n" 
                trans += "AM=M-1\n"
                trans += "D=M\n"
                trans += "@" + str(16+int(index)) + "\n"
                trans += "M=D\n"
            elif segment == "argument":
                trans += "@" + index + "\n"     
                trans += "D=A\n"                
                trans += "@ARG\n"               
                trans += "D=M+D\n"              
                trans += "@R13\n"               
                trans += "M=D\n"                
                trans += "@SP\n"                
                trans += "AM=M-1\n"             
                trans += "D=M\n"                
                trans += "@R13\n"               
                trans += "A=M\n"
                trans += "M=D\n"
            elif segment == "local":
                trans += "@" + index + "\n" 
                trans += "D=A\n"
                trans += "@LCL\n"
                trans += "D=M+D\n" 
                trans += "@R13\n"
                trans += "M=D\n"
                trans += "@SP\n"
                trans += "AM=M-1\n"
                trans += "D=M\n"
                trans += "@R13\n" 
                trans += "A=M\n"
                trans += "M=D\n"
            elif segment == "this":
                trans += "@" + index + "\n" 
                trans += "D=A\n"
                trans += "@THIS\n"
                trans += "D=M+D\n" 
                trans += "@R13\n"
                trans += "M=D\n"
                trans += "@SP\n" 
                trans += "AM=M-1\n"
                trans += "D=M\n"
                trans += "@R13\n"
                trans += "A=M\n"
                trans += "M=D\n"
            elif segment == "that":
                trans += "@" + index + "\n" 
                trans += "D=A\n"
                trans += "@THAT\n"
                trans += "D=M+D\n" 
                trans += "@R13\n"
                trans += "M=D\n"
                trans += "@SP\n" 
                trans += "AM=M-1\n"
                trans += "D=M\n"
                trans += "@R13\n" 
                trans += "A=M\n"
                trans += "M=D\n"
            elif segment == "temp":
                trans += "@" + index + "\n" 
                trans += "D=A\n"
                trans += "@5\n"
                trans += "D=A+D\n" 
                trans += "@R13\n"
                trans += "M=D\n"
                trans += "@SP\n"
                trans += "AM=M-1\n"
                trans += "D=M\n"
                trans += "@R13\n" 
                trans += "A=M\n"
                trans += "M=D\n"
        else:
            trans += segment + " //No ha sido implementado aun.\n"
        self.writen(trans)
    #Escribir en el documento de salida las traducciones creadas previamente.
    def writen(self, trans):
        salida = open(str(self.out) + ".asm", 'a')
        salida.write(trans)
        salida.close()


