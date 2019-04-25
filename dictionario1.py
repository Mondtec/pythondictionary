'''personal_data = {

    "nombre":"Oswaldo",
    "apellido_paterno": "Peralta",
    "edad":26,
    "sexo":"hombre"
}
print(personal_data)'''


'''paises = {
    "Mexico":"Norte America",
    "Colombia": "Sudamérica",
    "España":"Europa"
}
for y in paises:

    x = paises[y]
    print(x)'''

'''estados = {

    "Toluca":"Edo. de Mexico",
    "Campeche": "Campeche",
    "Saltillo": "Coahuila",
    "Monterrey":"Nuevo Leon"
}
obtencion = estados["Saltillo"]
print(obtencion)'''


'''cat_paises = {
    'Colombia':'COL',
    'Mexico':'MEX',
    'Peru':'PER',
    'Alemania':'ALE'
}
for x in cat_paises:

    print(x) #IMPRIME COLOMBIA, MEXICO,PERU, ALEMANIA
    print("----------------------------------------------")

for y in cat_paises:
    x = cat_paises[y]
    print(x)'''


''' IMPRIME SOLAMENTE LAS CLAVES DEL DICCIONARIO
monedas = {
    "Dólar de Barbados":"BBD",
    "Dólar de Belice":"BZD",
    "Dolar Canadiense":"CAD",
    "Franco Suizo":"CHF"
}

for recorredor in monedas:
    print(recorredor)
'''

''' IMPRIME SOLAMENTE LOS VALORES DEL DICCIONARIO
monedas = {
    "Dólar de Barbados":"BBD",
    "Dólar de Belice":"BZD",
    "Dolar Canadiense":"CAD",
    "Franco Suizo":"CHF"
}
for recorredor in monedas:
    print(monedas[recorredor])
'''


'''  IMPRIME SOLAMENTE LOS VALORES DEL DICCIONARIO
monedas = {
    "Dólar de Barbados":"BBD",
    "Dólar de Belice":"BZD",
    "Dolar Canadiense":"CAD",
    "Franco Suizo":"CHF",
    "Dólar de las Islas Caimán":"KYD"
}
for recorredor in monedas.values():
    print(recorredor)
'''

''' IMPRIME TANTO CLAVE COMO VALOR DEL DICCIONARIO
monedas = {
    "Dólar de Barbados":"BBD",
    "Dólar de Belice":"BZD",
    "Dolar Canadiense":"CAD",
    "Franco Suizo":"CHF",
    "Dólar de las Islas Caimán":"KYD"
}
for x,y in monedas.items():
    print(x,y)
'''

'''
monedas = {
    "Peso chileno":"CLP",
    "Peso Colombiano":"COP",
    "Peso Convertible":"CUC",
    "Peso Cubano":"CUP",
    "Peso Dominicano":"DOP",
    "Peso Mexicano":"MXN",
    "Peso filipino":"PHP",
    "Peso Uruguay en Unidades Indexadas (URUIURUI)":"UYI"
}

if "Peso Mexicano" in monedas:
    print("La moneda es válida")

'''

'''
monedas = {
    "Peso chileno":"CLP",
    "Peso Colombiano":"COP",
    "Peso Convertible":"CUC",
    "Peso Cubano":"CUP",
    "Peso Dominicano":"DOP",
    "Peso Mexicano":"MXN",
    "Peso filipino":"PHP",
    "Peso Uruguay en Unidades Indexadas (URUIURUI)":"UYI"
}
print("El catálogo actual de monedas del SAT es de:"+str(len(monedas)))

'''
'''
#AGREGANDO ELEMENTOS

monedas = {
    "PESO MEXICANO":"MXN",
    "DOLAR":"DLS",
    "EURO":"EUR",
    "FRANCO":"FRA",
    "FRANCO SUIZO":"FRS",
    "SOL":"SOL",
    "QUETZAL":"QUE",
    "YEN CHINO":"YEN",
}

monedas["BITCOIN"] = "BIT"
monedas["DOLAR CANADIENSE"] = "CAN"

for x,y in monedas.items():
    print("La moneda es: "+x)
    print("La clave es: "+y)
    print("--------------------------")
'''

'''
#REMOVIENDO ITEMS

monedas = {
   "PESO MEXICANO":"MXN",
    "DOLAR":"DLS",
    "EURO":"EUR",
    "FRANCO":"FRA",
    "FRANCO SUIZO":"FRS",
    "SOL":"SOL",
    "QUETZAL":"QUE",
    "YEN CHINO":"YEN",
}
monedas["BITCOIN"] = "BIT"
monedas["DOLAR CANADIENSE"] = "CAN"
monedas["PESO VERACRUZANO"] = "VER"


monedas.pop("PESO VERACRUZANO")

for x, y in monedas.items():
    print("La moneda es: "+x)
    print("La clave es: "+y)
    print("--------------------------")
    '''

'''
monedas = {
    "PESO COLOMBIANO":"COL",
    "PESO ARGENTINO":"ARG",
    "PESO MEXICANO":"MXN",
    "PESO CHILENO":"CHI"
}
monedas.popitem()
print(monedas)
'''

'''
monedas = {
    "PESO COLOMBIANO":"COL",
    "PESO ARGENTINO":"ARG",
    "PESO MEXICANO":"MXN",
    "PESO CHILENO":"CHI"
}

del monedas["PESO ARGENTINO"]
print(monedas)
'''

'''
monedas = {
    "PESO COLOMBIANO":"COL",
    "PESO ARGENTINO":"ARG",
    "PESO MEXICANO":"MXN",
    "PESO CHILENO":"CHI" 
}
del monedas
print(monedas)
'''

'''
#LIMPIANDO DICCIONARIO
monedas = {
    "PESO COLOMBIANO":"COL",
    "PESO ARGENTINO":"ARG",
    "PESO MEXICANO":"MXN",
    "PESO CHILENO":"CHI" 
}
monedas.clear()
print(monedas)
'''

'''
#COPIANDO UN DICCIONARIO
monedas = {
   "PESO MEXICANO":"MXN",
    "DOLAR":"DLS",
    "EURO":"EUR",
    "FRANCO":"FRA",
    "FRANCO SUIZO":"FRS",
    "SOL":"SOL",
    "QUETZAL":"QUE",
    "YEN CHINO":"YEN",
}

monedas2 = monedas.copy()
print("COPIA DE MONEDAS A MONEDAS 2: \n")
print(len(monedas2))

monedas2["PESO CHILENO"] = "CHI"
monedas2["PESO COLOMBIANO"] = "COL"
monedas2["PESO ARGENTINO"] = "ARG"
print("DICCIONARIO ORIGINAL: \n")
print(len(monedas))
print("DICCIONARIO MONEDAS 2 CON NUEVOS ELEMENTOS:\n")
print(len(monedas2))
'''

'''
c_paises = {
    "Mexico":"MEX",
    "España":"ESP",
    "COLOMBIA":"COL",
    "URUGUAY":"URU",
    "BRASIL":"BRA",
}
c_paises2 = dict(c_paises)
print(len(c_paises2))


c_paises2["Estados Unidos"] = "USA"
c_paises2["Peru"] = "PER"

print(len(c_paises2))
'''

'''
#OTRA FORMA DE CREAR DICCIONARIOS

c_paises = dict(Mexico="MEX", Colombia="COL",ESPAÑA="ESP",PERU="PER")
print(c_paises)
'''

'''
#USAR EL METODO GET PARA IMPRIMIR EL VALOR DE LA LLAVE MODELO DEL DICCIONARIO CARRO

carro = {
    "marca":"FORD",
    "modelo":"MUSTANG",
    "año":1964
}

print(carro.get("modelo"))
'''
'''
#CAMBIAR EL AÑO DE 1964 A 2018

carro = {
    "marca":"FORD",
    "modelo":"MUSTANG",
    "anio":1964
}
carro["anio"] = 2018
print(carro)
'''
'''
carro = {
    "marca":"FORD",
    "modelo":"MUSTANG",
    "anio": 1964
}
carro["color"]= "rojo"
print(carro)
'''
'''
#USA EL METODO POP PARA REMOVER LA LLAVE MODELO DEL DICCIONARIO CARRO

carro = {
    "marca":"FORD",
    "modelo":"MUSTANG",
    "anio":1964,
}
carro.pop("modelo")
print(carro)
'''

#USA EL METODO CLEAR PARA VACIAR EL DICCIONARIO CARRO

carro = {
    "marca":"FORD",
    "modelo":"MUSTANG",
    "anio":1964
}
carro.clear()
print(carro)

