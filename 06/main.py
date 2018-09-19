import Assembler
import sys
class main():
    def main():
        infile = ""
#        if len(sys.argv) != 1:
        print("Usage: Assembler.py file.asm")
#        else:
        infile = str(sys.argv[1])
        print(infile)
        asm = Assembler.Assembler(infile)
        asm.assemble()
    main()