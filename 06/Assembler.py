import Code
import Parser
import SymbolTable

class Assembler(object):
    
    def __init__(self, infile):
        self.infile = infile
        self.archive = ''
        self.symbol_table = SymbolTable.SymbolTable()
        self.symbol_address = 16       
    
    def firstpass(self):
        parser = Parser.Parser(self.infile)
        address = 0
        while parser.hasMoreCommands():
          parser.advance()
          if parser.commandType() == parser.A_COMMAND or parser.commandType() == parser.C_COMMAND:
            address += 1
          elif parser.commandType() == parser.L_COMMAND:
            self.symbol_table.add_entry(parser.symbol(), address)
              
    def secondpass(self):
        parser = Parser.Parser(self.infile)
        code = Code.Code()
        while parser.hasMoreCommands(): 
          parser.advance()
          #Para comandos tipo A
          if parser.commandType() == parser.A_COMMAND:
            a = str(parser.symbol())
            if a.isdigit(): 
              writeCommand = self.aCommando(a)
              self.write(writeCommand)
              self.symbol_address += 1
            elif not self.symbol_table.contains(a) and not a.isdigit():
              self.symbol_table.add_entry(parser.symbol(),self.symbol_address)
              writeCommand = self.aCommando(parser.symbol())
              self.write(writeCommand)
              self.symbol_address += 1
            elif self.symbol_table.contains(parser.symbol()): 
              writeCommand = self.aCommando(parser.symbol())
              self.write(writeCommand)
          #Para comandos tipo C
          elif parser.commandType() == parser.C_COMMAND:
            writeCommand = self.cCommando(parser,code)
            self.write(writeCommand)
            self.symbol_address += 1
            
    def aCommando(self, symbol):
      if not str(symbol).isdigit():
        a = self.symbol_table.get_address(symbol)
        binary = '{0:b}'.format(a)
        binlen = len(binary)
        for i in range(15 - binlen):
          binary = '0' + binary
        return "0"+binary
      else:
        binary = '{0:b}'.format(int(symbol))
        binlen = len(binary)
        for i in range(15 - binlen):
          binary = '0' + binary
        return '0'+binary    
    
    def cCommando(self, parser, code):
        comp = parser.comp() 
        dest = parser.dest() 
        jump = parser.jump() 
        codeComp = code.comp(comp)
        codeDest = code.dest(dest)
        codeJump = code.jump(jump)
        return '111'+codeComp+codeDest+codeJump
      
    def write(self, linea):
        salida = open(self.archive + '.hack','a')
        salida.write(linea+'\n')
        salida.close()      

    def assemble(self):
        self.firstpass()
        if(self.infile.endswith('.asm')):
          pos2 = self.infile.find('.')
          self.archive = self.infile[0:pos2]
          out = open(self.archive + '.hack','w+')
          print(out)
        self.secondpass()