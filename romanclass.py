class RomanNumber():
    
    simbolos = {
    "unidades": ["","I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"],
    "decenas": ["", "X", "XX", "XXX", "LX", "L", "LX", "LXX", "LXXX", "XC"],
    "centenas": ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"],
    "millares": ["", "M", "MM", "MMM"]
    }
    
    Numeros_romanos = { 
    "I" : 1, "V" : 5, "X" : 10, "L": 50, "C": 100, "D": 500, "M": 1000
    }
    
    def __init__(self, valor):
        
        if isinstance(valor, int):
            self.valor = valor
            self.cadena = self.convRomanos()

        if isinstance(valor, str):
            self.cadena = valor
            self.valor = self.convSimbolos()

 
    def validar(self):
        #isinstance(n, int) -> valida si n es un int (valida que n sea del tipo indicado)
        if not isinstance(self.valor, int):
            #   raise ValueError lanza el error
            raise ValueError("{} debe ser un numero entero".format(self.valor))
        if self.valor < 0 or self.valor > 3999:
            raise ValueError("{} debe estar entre 0 y 3999".format(self.valor))
    
    def convSimbolos(self):
        acumulador = 0
        valor_ant = 0
        repeticion = 0
        mayor = 0 
        for caracter in self.cadena:
            valor = self.Numeros_romanos.get(caracter) #comprueba si el caracter esta en la lista, si falla suelta None
            if not valor:
                raise ValueError("Error que sea")

            if valor_ant and valor > valor_ant:
                if valor_ant in (5, 50, 500):
                    raise ValueError("No se pueden restar V, L o D")

                if valor_ant > 0 and valor> valor_ant * 10:
                    raise ValueError("No se admiten restas en digitos 10 veces mayores")

                if repeticion > 0: #Al poner repeticion > 0 al inicio del bucle me aseguro que no tiene valor 0 al cambiar de caracter si se ha repetido antes
                    raise ValueError("No se pueden restar dos iguales")
                
                mayor +=1

                if mayor > 1:
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

    def convRomanos(self):

        self.validar()
        
        c = str(self.valor)
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
        return self.simbolos["millares"][millares] + self.simbolos["centenas"][centenas] + self.simbolos["decenas"][decenas] + self.simbolos["unidades"][unidades]

    def __str__(self):
        return self.cadena
    
    def __repr__(self):
        return self.__str__()
    def __len__(self):
        return len(self.cadena)
    def __eq__(self, other):
        if isinstance(other, RomanNumber):
            return self.valor== other.valor
        if isinstance(other, int):
            return self.valor == other
        if isinstance(other, float):
            return self.valor == other
        if isinstance(other, str):
            return self.cadena == other
        raise ValueError("{} solo puede ser entero, cadena, flotante o RomanNumber".format(other))
    
    def __lt__(self, other):
        if isinstance(other, RomanNumber):
            return self.valor <= other.valor
        if isinstance(other, int):
            return self.valor <= other
        if isinstance(other, float):
            return self.valor <= other
        if isinstance(other, str):
            return self.cadena <= other
        raise ValueError("{} solo puede ser entero, cadena, flotante o RomanNumber".format(other))
    def __lte__(self, other):
        if isinstance(other, RomanNumber):
                return self.valor <= other.valor
        if isinstance(other, int):
            return self.valor <= other
        if isinstance(other, float):
            return self.valor <= other
        if isinstance(other, str):
            return self.cadena <= other
        raise ValueError("{} solo puede ser entero, cadena, flotante o RomanNumber".format(other))
    #def __gt__(self, other):
    
    #def __gte__(sel, other):
