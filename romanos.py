simbolos={
    "unidades": ["","I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"],
    "decenas": ["", "X", "XX", "XXX", "LX", "L", "LX", "LXX", "LXXX", "XC"],
    "centenas": ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"],
    "millares": ["", "M", "MM", "MMM"]
}

Numeros_romanos = { 
    "I" : 1, "V" : 5, "X" : 10, "L": 50, "C": 100, "D": 500, "M": 1000
    }

def validar(n):


    #isinstance(n, int) -> valida si n es un int (valida que n sea del tipo indicado)
    if not isinstance(n, int):
        #   raise ValueError lanza el error
        raise ValueError("{} debe ser un numero entero".format(n))
    if n < 0 or n > 3999:
        raise ValueError("{} debe estar entre 0 y 3999".format(n))

def convRomanos(n):

    validar(n)
    
    c = str(n)
    #c ="{:0d4}".format(n)
    
    unidades = decenas = centenas = millares = 0
    if len(c) >= 1:
        unidades= int(c[-1])
    if len(c) >= 2:
        decenas = int(c[-2])
    if len(c) >= 3:
        centenas = int(c[-3])
    if len(c) >= 4:
        millares = int(c[-4])
    #return millares, centenas, decenas, unidades
    componentes = (millares, centenas, decenas, unidades)
    return simbolos["millares"][millares] + simbolos["centenas"][centenas] + simbolos["decenas"][decenas] + simbolos["unidades"][unidades]


def conversor(entrada):
    cadena = ""
    while entrada > 0:
        if entrada - 1000 >= 0:    
            cadena+="M"
            entrada -=1000
        elif entrada - 900 >=0:
            cadena+="CM"
            entrada -=900
        elif entrada - 500 >= 0:
            cadena+="D"
            entrada -=500
        elif entrada - 400 >=0:
            cadena+="CD"
            entrada -=400
        elif entrada - 100 >= 0:
            cadena+="C"
            entrada -=100
        elif entrada - 90 >=0:
            cadena+="XC"
            entrada -=90
        elif entrada - 50 >= 0:
            cadena+="L"
            entrada -=50
        elif entrada - 40 >= 0:
            cadena+="XL"
            entrada -=40
        elif entrada - 10 >= 0:
            cadena+="X"
            entrada -=10
        elif entrada - 9 >= 0:
            cadena+="IX"
            entrada -=9
        elif entrada - 5 >= 0:
            cadena+="V"
            entrada -=5
        elif entrada - 4 >= 0:
            cadena+="IV"
            entrada -= 4
        else:
            cadena+="I"
            entrada -=1
            #count +=1
    return cadena

def convSimbolos(n):
    acumulador = 0
    valor_ant = 0
    repeticion = 0
    mayor = 0 
    for caracter in n:
        valor = Numeros_romanos[caracter]

        if valor> valor_ant:
            if valor_ant in (5, 50, 500):
                raise ValueError("No se pueden restar V, L o D")

            if valor_ant > 0 and valor> valor_ant * 10:
                raise ValueError("No se admiten restas en digitos 10 veces mayores")

            if repeticion > 0: #Al poner repeticion > 0 al inicio del bucle me aseguro que no tiene valor 0 al cambiar de caracter si se ha repetido antes
                raise ValueError("No se pueden restar dos iguales")
            
            mayor +=1

            if mayor > 2:
                raise ValueError("Has pikao")
            

            acumulador -= valor_ant
            acumulador += valor - valor_ant
        else:
            acumulador += valor
            mayor = 0

        if valor == valor_ant:
            if valor_ant in (5, 50, 500):
                raise ValueError("No puede usarse el caracter {} dos veces".format(caracter))
            repeticion += 1
            if repeticion == 3:
                raise ValueError("No se puede poner 4 veces el simbolo {}".format(caracter))
        else:
            repeticion = 0

        valor_ant = valor

    return acumulador


#muestra = int(input("Introduzca numero: "))
#print(convRomanos(muestra))
#resultado = conversor(muestra)
#print ("El numero romano resultante es: ", resultado)

