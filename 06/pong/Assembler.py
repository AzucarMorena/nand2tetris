import sys
import string
import os
import glob
import argparse

def main():
    #Main

    # analizar los argumentos para obtener el nombre de archivo
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', nargs='?')
    args = parser.parse_args()
    
    if(args.filename is None):
        print('Una vez compilado el programa dirijase la carpeta, escribe .\Assembler.py seguido del archivo')
        return
        
    file = os.path.abspath(args.filename)    
           
    symbol_table = {'R0':'0', 'R1':'1', 'R2':'2', 'R3':'3', 'R4':'4',
                    'R5':'5', 'R6':'6', 'R7':'7', 'R8':'8', 'R9':'9',
                    'R10':'10', 'R11':'11', 'R12':'12', 'R13':'13', 'R14':'14', 'R15':'15',
                    'SP':'0', 'LCL':'1', 'ARG':'2', 'THIS':'3',
                    'THAT':'4', 'SCREEN':'16384', 'KBD':'24576'}
    
    symbol_table['variableR'] = 16

    with open(file.split('.')[0] + '.hack', 'w') as output:

        # Primer Paso
        with open(file, 'r') as asm:
            counter = 0
            for line in asm:
                line = clean_line(line, ['//'])
                ct = get_command_type(line)
                if ct in ['A_COMMAND', 'C_COMMAND']:
                    counter += 1
                elif ct in ['L_COMMAND']:
                    symbol_table[line.strip('()')] = str(counter)

        # Segundo Paso 
        with open(file, 'r') as asm:
            for line in asm:
                line = clean_line(line, ['//','('])
                ct = get_command_type(line)
                if ct in ['A_COMMAND']:
                    commandT = translate_a_command(line, symbol_table) + '\n'
                elif ct in ['C_COMMAND']:
                    commandT = translate_c_command(line) + '\n'
                else:
                    commandT = ''
                output.write(commandT)

def clean_line(line, sep):
    # Eliminacion de comentarios
    for s in sep:
        line = line.split(s)[0]
    return line.strip()
            
def get_command_type(line):
    # Identificacion del comando
    if line in ['']:
        return ''
    elif line[0] in ['@']:
        return 'A_COMMAND'
    elif line[0] in ['(']:
        return 'L_COMMAND'
    else:
        return 'C_COMMAND'

def translate_a_command(line,symbol_table):
    # Traduccion de a_command a codigo de maquina
    line = line[1:]
    if not line.isdigit():
        if line not in symbol_table:
            symbol_table[line] = symbol_table['variableR']
            symbol_table['variableR'] += 1
        instruction = '0' + bin(int(symbol_table[line]))[2:].zfill(15)
    else:
        instruction = '0' + bin(int(line))[2:].zfill(15) 
    return instruction

def translate_c_command(line):
    # Traduccion de c_command a codigo de maquina
    if '=' in line and ';' in line:
        instruction = ''
    elif '=' in line:
        dest,comp = line.split('=')
        dest,comp = dest.strip(),comp.strip()
        instruction = '111' + lookup_comp(comp) + lookup_dest(dest) + '000'
    elif ';' in line:
        comp,jmp = line.split(';')
        comp,jmp = comp.strip(),jmp.strip()
        instruction = '111' + lookup_comp(comp) + '000' + lookup_jmp(jmp)
    else:
        instruction = ''
    return instruction

def lookup_dest(asm):
    d = {'':'000', 'M':'001', 'D':'010', 'MD':'011',
         'A':'100', 'AM':'101', 'AD':'110', 'AMD':'111'}
    return d[asm]

def lookup_comp(asm):
    c = {'0':'0101010', '1':'0111111', '-1':'0111010', 'D':'0001100',
         'A':'0110000', '!D':'0001101', '!A':'0110001', '-D':'000111',
         '-A':'0110011', 'D+1':'0011111', 'A+1':'0110111','D-1':'0001110',
         'A-1':'0110010', 'D+A':'0000010', 'D-A':'0010011', 'A-D':'0000111',
         'D&A':'0000000', 'D|A':'0010101', 'M':'1110000', '!M':'1110001',
         '-M':'1110011', 'M+1':'1110111', 'M-1':'1110010', 'D+M':'1000010',
         'D-M':'1010011', 'M-D':'1000111', 'D&M':'1000000', 'D|M':'1010101'}
    return c[asm]

def lookup_jmp(asm):
    j = {'':'000', 'JGT':'001', 'JEQ':'010', 'JGE':'011',
         'JLT':'100', 'JNE':'101', 'JLE':'110', 'JMP':'111'}
    return j[asm]


if __name__ == '__main__':
    sys.exit(main())