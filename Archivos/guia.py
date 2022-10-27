import os 
archivo = "temp.txt"
f = open(archivo, 'r')
#print(f.read())
lineas  = f.readlines()
y = []
nombres={}
valores={}
saldos={}
nrolineas = 0
for linea in lineas:
    nrolineas += 1
pos=0
for linea in lineas:
    pos = pos + 1
    y = linea.split(" ")
    codigo = y[0]
    nombres.setdefault(codigo, y[1])
    valores.setdefault(codigo, y[2])
    saldo = y[3]
    if pos!=nrolineas:
        p1 = len(saldo) - 1
        saldos.setdefault(codigo, saldo[0:p1])
    else:
        saldos.setdefault(codigo,saldo)
f.close()