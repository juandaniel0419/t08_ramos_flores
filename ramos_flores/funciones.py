# ejercicio 1

msg="LAS MATEMATICAS Y LA FISICA SON LA BASE DE TODA INGENIERIA"
print(msg.count("A")) # mostrara las veces que se repita la palabra A }
print("")


# ejercicio 2
msg="SI VIENES MAÑANA TE BAÑAS SI POR FAVOR"
print(msg.lower())  # mostrara las cadena en minusculas
print("")


# ejercicio 3
msg="no vengas sin REGALO OK!"
print(msg.upper()) # mostrara la cadena en mayusculas
print("")


#ejercicio 4
msg="Y SI ESTUDIAS MEDICINA, PERO SI ESTUDIAS INGENIERIA  PODRIAS TAMBIEN ESTUDIAR DERECHO"
print(msg.replace("ESTUDIAS","JALAS")) # mostrara la cadena pero solo cambiara ESRUDIAS por JALAS
print("")


#  ejercicio 5
msg="HUGO Y JAIME SALDRAN A UNA FIESTA EN CHICLAYO"
text=msg.replace("HUGO","carlos").lower().replace("JAIME","maria")
print(text)
print("")


# ejercicio 6
msg="              JUAN   NO IRA A  LA FIESTA POR QUE SE  MURIO SU PERRO"
print(msg.lstrip()) # hubicara a la cadena sin espacios al empezar
print("")


# ejercicio 7
msg="12345678hjk456789"
print(msg.isdigit()) # mostrara False ya que no la cadena no es un digito
print("")


# ejercicio 8
msg="47ier54yty8ly34"
print(msg.isalnum()) # mostrara True ya que la cadena es alfanumerica
print("")

# ejercicio 9
msg="1929kk31" # mostrara True si lo que buscas es alfabeto
print(msg.isalpha())
print("")

# ejercicio 10
msg="juan maria marcos daniel"
nombres=msg.split(" ")   # separara los nombres por el espacio
for item in nombres:
    print(item.upper())

# ejercicio 11
msg="juana la cuabna se ahogo      "
print(msg.rstrip())

# ejercicio 12
msg="juajsdsadbafdi"
print(msg.title())

# ejercicio 13
msg="juan y maria se casaron por el padre pedro ,pero juan dejo plantada a maria por luz"
print(msg.replace("juan","pedro").upper())
print("")


# ejercicio 14
msg="YA ME CANSE HACER EL TRABAJO DE PROGRAMACION IRE A DORMIR "
print(msg[::-1])

# ejercicio 15
msg="NUNCA DEJES UNA TAREA PARA ULTIMO MOMENTO APRENDRE COMO YO "
print(msg.replace("APRENDE"," "))
