import imgToBits as itb

def lfsr(lonFinal, seed, taps):
    # Resultado y sr con la semilla inicial
    res = ''
    sr = seed

    # Se acaba el ciclo cuando se llegue a la long requerida
    while len(res) < lonFinal:
        xor = 0

        # Hacemos xor con cada num en taps
        for t in taps:
            xor ^= int(sr[t-1]) 
        res += str(xor)
        
        # Contateno el xor al inicio de la cadena
        # y elimino uno de la cadena anterior
        sr = str(xor) + sr[:-1]

    return res

resultado = lfsr(len(itb.img), '11001001', (8,7,6,1))