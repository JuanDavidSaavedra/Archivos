import os
from datetime import datetime
archivo = 'factura.txt'
f = open(archivo, 'w')
productos = {1:["Asesoría", 10000], 2: ["Desarrollo", 50000], 3:["Tester", 25000]}
f.write("              EMPRESA DATOS Y PROCESOS CORPORATIVOS" + '\n')
no = input("Digite nombre del cliente: ")
fecha=datetime.now()
f.write(" Fecha: " + str(fecha) + '\n' + "Cliente: " + no + '\n')
f.write("------------------------------------------------------------------------------" '\n')
f.write("Código     Nombre     Cantidad     Valor Unitario     Valor Total" '\n')
f.write("------------------------------------------------------------------------------" '\n')
print("Listado de productos")
print(productos)
n = int(input("Digite la cantidad de productos: "))
acu = 0
acu1 = 0
for i in range(n):
    x = int(input("Digite el código del producto: "))
    y = int(input("Digite la cantidad del producto: "))
    acu = y*productos[x][1]
    acu1 = acu1 + acu
    f.write(str(x) + "     " + productos[x][0] + "     " + str(y) + "     " + str(productos[x][1]) + "     " + str(acu) + '\n')
f.write("------------------------------------------------------------------------------" '\n')
f.write("TOTAL FACTURA: " + str(acu) + '\n')
f.close()
os.system("notepad.exe factura.txt")
