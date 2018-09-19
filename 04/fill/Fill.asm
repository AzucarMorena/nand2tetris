// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.
(CICLO)
    @8192                  
    D = A               // D = 8192     
    @i
    M = D               // i = 8192 (tamaño de la pantalla)
    @SCREEN
    D = A               // D = 16384 (primera posicion de la pantalla)
    @i
    D = D + M           // D = 16384 + 8192
    @x
    M = D               // RAM[x] = 24576 
    @KBD
    D = M
    @BLANCO
    D;JEQ

(NEGRO)
    @i                  
    D = M               // D = RAM[i]
    @CICLO    
    D;JLT               // D <= 0 (Ya la pantallla esta negra) 

    @x     
    D = M               // D = RAM[x]
    A = D             
    M = - 1             // RAM[D] = -1 (pintamos esa posicion de la pantalla de negro)
    @i              
    M = M - 1           // RAM[i] = (disminuimos la posicion de la pantalla)
    @x
    M = M -1
    @NEGRO
    0;JMP

(BLANCO)
    @i                  
    D = M               // D = RAM[i]
    @CICLO    
    D;JLT               // D <= 0 (Ya la pantallla esta negra) 

    @x     
    D = M               // D = RAM[x]
    A = D             
    M = 0             // RAM[D] = -1 (pintamos esa posicion de la pantalla de negro)
    @i              
    M = M - 1           // RAM[i] = (disminuimos la posicion de la pantalla)
    @x
    M = M -1
    @BLANCO
    0;JMP