import sys, os, CodeWriter, Parser

class Main:
    def main():
        infile = ""
        print("Usage: Main.py <file> without extension")
        infile = str(sys.argv[1])
        ins = open (infile + ".vm")
        parser = Parser.Parser(infile)
        outfile = open(infile + ".asm", 'w+')
        codewr = CodeWriter.CodeWriter(infile)
        while parser.hasMoreCommands():
            parser.advance()
            cd = parser.command
            commandType = parser.aux
            if commandType == "push" or commandType == "pop":
                codewr.writePushPop(parser.aux, parser.arg1(), parser.arg2())
            else:
                codewr.writeAritmethic(parser.aux)
        if not parser.hasMoreCommands():
            trans = "(END)\n"
            trans += "@END\n"
            trans += "D;JMP"
            outfileaux = open(infile + ".asm", 'a')
            outfileaux.write(trans)
            outfileaux.close
    
    main()
