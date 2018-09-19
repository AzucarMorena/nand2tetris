    @16384
    D = A
    @i
    M = D
(HORIZONTAL)
    @i
    D = M
    @16387
    D = D - A
    @END
    D;JGT
    @32767
    D = A
    @i
    M = D
    @i
    M = M - 1
    @LOOP
    0;JMP
(END)
    @i