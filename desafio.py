# PARTE MARIA - NÚMERO DE EULER


# PARTE GUSTAVO - SENO


# PARTE IGOR - COSSENO


# PARTE YASMIN - LOG NATURAL


# PARTE PEDRO - EXPONENCIAL

def exponencial (x, termos=50):
    termo_atual = 1.0
    resultado = 1
    
    for i in range (1, termos):
        termo_atual = termo_atual * x / i
        resultado += termo_atual
        
    return resultado

x = float(input("digite seu numero: "))

print(exponencial(x))

# PARTE GUILHERME - PI

