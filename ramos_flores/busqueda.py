# Busquedas de cadenas

# Ejercicio (PARSER)
# Ingresar el codigo numerico
# 1 -> hola
# 2 -> como estas
# 3 -> te quiero

# Ingresar un comando de 4 codigos numerico

comando="12333"

cmd1=comando[0]
cmd2=comando[1]
cmd3=comando[2]
cmd4=comando[3]
code=""
#                     1         2
#           01234567890123456789012345678
sentencias="hola como estas te quiero"
print(sentencias.find("quiero"))
hola=sentencias[0:4]
como_estas=sentencias[5:15]
te_quiero=sentencias[16:]

# Primer Bloque para el Codigo
if (cmd1 == '1'):
    code=hola
if (cmd1 == '2'):
    code=como_estas
if (cmd1 == '3'):
    code=te_quiero

# 2do bloque para el codigo
if (cmd2 == '1'):
    code += "\n" + hola
if (cmd2 == '2'):
    code += "\n" + como_estas
if (cmd2 == '3'):
    code += "\n" + te_quiero


# 3cer bloque para el codigo
if (cmd3 == '1'):
    code += "\n" + hola
if (cmd3 == '2'):
    code += "\n" + como_estas
if (cmd3 == '3'):
    code += "\n" + te_quiero

# 4to bloque para el codigo
if (cmd4 == '1'):
    code += "\n" + hola
if (cmd4 == '2'):
    code += "\n" + como_estas
if (cmd4 == '3'):
    code += "\n" + te_quiero

print(code)
print("")



# ejercicio 2

comando = "13254"

cmd1 = comando[0]
cmd2 = comando[1]
cmd3 = comando[2]
cmd4 = comando[3]
cmd5 = comando[4]
code = ""
#                      1         2         3         4
#            01234567890123456789012345678901234567890123
sentencias ="papa y tu mama no te quieren y ellos viajaran"

papa= sentencias[0:4]
y= sentencias[4:6]
tu = sentencias[7:9]
mama=sentencias[10:14]
quieren=sentencias[21:29]

# Primer Bloque para el Codigo
if (cmd1 == '1'):
    code = papa
if (cmd1 == '2'):
    code = mama
if (cmd1 == '3'):
    code = tu
if(cmd1 == '4'):
    code= y
if(cmd1 =='5'):
    code = quieren

# 2do bloque para el codigo
if (cmd2 == '1'):
    code += "\n" + papa
if (cmd2 == '2'):
    code += "\n" + mama
if (cmd2 == '3'):
    code += "\n" + tu
if(cmd2 == '4'):
    code+="\n"+ y
if(cmd2 =='5'):
    code +="\n"+ quieren

# 3cer bloque para el codigo
if (cmd3 == '1'):
    code += "\n" + hola
if (cmd3 == '2'):
    code += "\n" + como_estas
if (cmd3 == '3'):
    code += "\n" + te_quiero
if(cmd3 == '4'):
    code+="\n"+ y
if(cmd3 =='5'):
    code +="\n"+ quieren

# 4to bloque para el codigo
if (cmd4 == '1'):
    code += "\n" + hola
if (cmd4 == '2'):
    code += "\n" + como_estas
if (cmd4 == '3'):
    code += "\n" + te_quiero
if(cmd4 == '4'):
    code+="\n"+ y
if(cmd4 =='5'):
    code +="\n"+ quieren

# 5to bloque para el codigo
if (cmd5 == '1'):
    code += "\n" + hola
if (cmd5 == '2'):
    code += "\n" + como_estas
if (cmd5 == '3'):
    code += "\n" + te_quiero
if(cmd5 == '4'):
    code+="\n"+ y
if(cmd5 =='5'):
    code +="\n"+ quieren

print(code)


# ejercicio 3


comando="3411"

cmd1=comando[0]
cmd2=comando[1]
cmd3=comando[2]
cmd4=comando[3]
code=""
#                     1         2
#           01234567890123456789012345678
sentencias="si no vas conmigo con el"

x=sentencias[0:2]
y=sentencias[3:5]
z=sentencias[6:9]
w=sentencias[10:17]
v=sentencias[18:21]

# Primer Bloque para el Codigo
if (cmd1 == '1'):
    code+=x
if (cmd1 == '2'):
    code+=y
if (cmd1 == '3'):
    code+=z
if(cmd1 =='4'):
    code+=w
if(cmd1 =='5'):
    code +=v
#2do bloque para el codigo
if (cmd2 == '1'):
    code += "\n" + x
if (cmd2 == '2'):
    code += "\n" + y
if (cmd2 == '3'):
    code += "\n" + z
if (cmd2 == '4'):
    code += "\n" + w
if (cmd2 == '5'):
    code += "\n" + v

# 3cer bloque para el codigo
if (cmd3 == '1'):
    code += "\n" + x
if (cmd3 == '2'):
    code += "\n"+ y
if (cmd3 == '3'):
    code += "\n" + z
if (cmd3 == '4'):
    code += "\n" + w
if (cmd3 == '5'):
    code += "\n" + v
# 4to bloque para el codigo
if (cmd4 == '1'):
    code += "\n" + x
if (cmd4 == '2'):
    code += "\n" + y
if (cmd4 == '3'):
    code += "\n" + z
if (cmd4 == '4'):
    code += "\n" + w
if (cmd4 == '3'):
    code += "\n" + v
print(code)
print("")


# ejercicio 4
comando="1423"

cmd1=comando[0]
cmd2=comando[1]
cmd3=comando[2]
cmd4=comando[3]
code=""
#                     1         2
#           01234567890123456789012345678
sentencias="perro y gato gallina "

x=sentencias[0:5]
y=sentencias[6:7]
z=sentencias[8:12]
w=sentencias[13:]

# Primer Bloque para el Codigo
if (cmd1 == '1'):
    code+=x
if (cmd1 == '2'):
    code+=y
if (cmd1 == '3'):
    code+=z
if(cmd1 =='4'):
    code+=w


#2do bloque para el codigo
if (cmd2 == '1'):
    code += "\n" + x
if (cmd2 == '2'):
    code += "\n" + y
if (cmd2 == '3'):
    code += "\n" + z
if (cmd2 == '4'):
    code += "\n" + w


# 3cer bloque para el codigo
if (cmd3 == '1'):
    code += "\n" + x
if (cmd3 == '2'):
    code += "\n"+ y
if (cmd3 == '3'):
    code += "\n" + z


# 4to bloque para el codigo
if (cmd4 == '1'):
    code += "\n" + x
if (cmd4 == '2'):
    code += "\n" + y
if (cmd4 == '3'):
    code += "\n" + z
if (cmd4 == '4'):
    code += "\n" + w

print(code)
print("")



# ejercicio 5

comando="12345"

cmd1=comando[0]
cmd2=comando[1]
cmd3=comando[2]
cmd4=comando[3]
cmd5=comando[4]
code=""
#                     1
#           012345678901234
sentencias="200 + 300 = 500"

x=sentencias[0:3]
y=sentencias[4:5]
z=sentencias[6:9]
w=sentencias[10:11]
v=sentencias[12:]

# Primer Bloque para el Codigo
if (cmd1 == '1'):
    code+=x
if (cmd1 == '2'):
    code+=y
if (cmd1 == '3'):
    code+=z
if(cmd1 =='4'):
    code+=w
if(cmd1 =='5'):
    code +=v
#2do bloque para el codigo
if (cmd2 == '1'):
    code += "\n" + x
if (cmd2 == '2'):
    code += "\n" + y
if (cmd2 == '3'):
    code += "\n" + z
if (cmd2 == '4'):
    code += "\n" + w
if (cmd2 == '5'):
    code += "\n" + v

# 3cer bloque para el codigo
if (cmd3 == '1'):
    code += "\n" + x
if (cmd3 == '2'):
    code += "\n"+ y
if (cmd3 == '3'):
    code += "\n" + z
if (cmd3 == '4'):
    code += "\n" + w
if (cmd3 == '5'):
    code += "\n" + v
# 4to bloque para el codigo
if (cmd4 == '1'):
    code += "\n" + x
if (cmd4 == '2'):
    code += "\n" + y
if (cmd4 == '3'):
    code += "\n" + z
if (cmd4 == '4'):
    code += "\n" + w
if (cmd4 == '3'):
    code += "\n" + v
# 5to bloque para el codigo
if (cmd5 == '1'):
    code += "\n" + x
if (cmd5 == '2'):
    code += "\n" + y
if (cmd5 == '3'):
    code += "\n" + z
if (cmd5 == '4'):
    code += "\n" + w
if (cmd5 == '5'):
    code += "\n" + v
print(code)
print("")


# ejercicio 6
comando="14532"

cmd1=comando[0]
cmd2=comando[1]
cmd3=comando[2]
cmd4=comando[3]
cmd5=comando[4]
code=""
#                     1         2
#           0123456789012345678901234
sentencias="feliz navidad y año nuevo"

x=sentencias[0:5]
y=sentencias[6:13]
z=sentencias[14:15]
w=sentencias[16:19]
v=sentencias[20:]

# Primer Bloque para el Codigo
if (cmd1 == '1'):
    code+=x
if (cmd1 == '2'):
    code+=y
if (cmd1 == '3'):
    code+=z
if(cmd1 =='4'):
    code+=w
if(cmd1 =='5'):
    code +=v
#2do bloque para el codigo
if (cmd2 == '1'):
    code += "\n" + x
if (cmd2 == '2'):
    code += "\n" + y
if (cmd2 == '3'):
    code += "\n" + z
if (cmd2 == '4'):
    code += "\n" + w
if (cmd2 == '5'):
    code += "\n" + v

# 3cer bloque para el codigo
if (cmd3 == '1'):
    code += "\n" + x
if (cmd3 == '2'):
    code += "\n"+ y
if (cmd3 == '3'):
    code += "\n" + z
if (cmd3 == '4'):
    code += "\n" + w
if (cmd3 == '5'):
    code += "\n" + v
# 4to bloque para el codigo
if (cmd4 == '1'):
    code += "\n" + x
if (cmd4 == '2'):
    code += "\n" + y
if (cmd4 == '3'):
    code += "\n" + z
if (cmd4 == '4'):
    code += "\n" + w
if (cmd4 == '5'):
    code += "\n" + v
# 5to bloque para el codigo
if (cmd5 == '1'):
    code += "\n" + x
if (cmd5 == '2'):
    code += "\n" + y
if (cmd5 == '3'):
    code += "\n" + z
if (cmd5 == '4'):
    code += "\n" + w
if (cmd5 == '5'):
    code += "\n" + v
print(code)
print("")



# ejercicio 7

comando="15423"

cmd1=comando[0]
cmd2=comando[1]
cmd3=comando[2]
cmd4=comando[3]
cmd5=comando[4]
code=""
#                     1
#           012345678901234567890
sentencias="no por favor dejes me "

x=sentencias[0:2]
y=sentencias[3:6]
z=sentencias[7:12]
w=sentencias[13:18]
v=sentencias[19:]

# Primer Bloque para el Codigo
if (cmd1 == '1'):
    code+=x
if (cmd1 == '2'):
    code+=y
if (cmd1 == '3'):
    code+=z
if(cmd1 =='4'):
    code+=w
if(cmd1 =='5'):
    code +=v
#2do bloque para el codigo
if (cmd2 == '1'):
    code += "\n" + x
if (cmd2 == '2'):
    code += "\n" + y
if (cmd2 == '3'):
    code += "\n" + z
if (cmd2 == '4'):
    code += "\n" + w
if (cmd2 == '5'):
    code += "\n" + v

# 3cer bloque para el codigo
if (cmd3 == '1'):
    code += "\n" + x
if (cmd3 == '2'):
    code += "\n"+ y
if (cmd3 == '3'):
    code += "\n" + z
if (cmd3 == '4'):
    code += "\n" + w
if (cmd3 == '5'):
    code += "\n" + v
# 4to bloque para el codigo
if (cmd4 == '1'):
    code += "\n" + x
if (cmd4 == '2'):
    code += "\n" + y
if (cmd4 == '3'):
    code += "\n" + z
if (cmd4 == '4'):
    code += "\n" + w
if (cmd4 == '5'):
    code += "\n" + v
# 5to bloque para el codigo
if (cmd5 == '1'):
    code += "\n" + x
if (cmd5 == '2'):
    code += "\n" + y
if (cmd5 == '3'):
    code += "\n" + z
if (cmd5 == '4'):
    code += "\n" + w
if (cmd5 == '5'):
    code += "\n" + v
print(code)
print("")


# ejercicio 8

comando="12345"

cmd1=comando[0]
cmd2=comando[1]
cmd3=comando[2]
cmd4=comando[3]
cmd5=comando[4]
code=""
#                     1
#           012345678901234567890
sentencias="amor y odio dos pasos"

x=sentencias[0:4]   #amor
y=sentencias[3::-1] #roma
z=sentencias[5:6]   # y
w=sentencias[7:11]   #odio
v=sentencias[10:6:-1]   # oido

# Primer Bloque para el Codigo
if (cmd1 == '1'):
    code+=x
if (cmd1 == '2'):
    code+=y
if (cmd1 == '3'):
    code+=z
if(cmd1 =='4'):
    code+=w
if(cmd1 =='5'):
    code +=v
#2do bloque para el codigo
if (cmd2 == '1'):
    code += "\n" + x
if (cmd2 == '2'):
    code += "\n" + y
if (cmd2 == '3'):
    code += "\n" + z
if (cmd2 == '4'):
    code += "\n" + w
if (cmd2 == '5'):
    code += "\n" + v

# 3cer bloque para el codigo
if (cmd3 == '1'):
    code += "\n" + x
if (cmd3 == '2'):
    code += "\n"+ y
if (cmd3 == '3'):
    code += "\n" + z
if (cmd3 == '4'):
    code += "\n" + w
if (cmd3 == '5'):
    code += "\n" + v
# 4to bloque para el codigo
if (cmd4 == '1'):
    code += "\n" + x
if (cmd4 == '2'):
    code += "\n" + y
if (cmd4 == '3'):
    code += "\n" + z
if (cmd4 == '4'):
    code += "\n" + w
if (cmd4 == '5'):
    code += "\n" + v
# 5to bloque para el codigo
if (cmd5 == '1'):
    code += "\n" + x
if (cmd5 == '2'):
    code += "\n" + y
if (cmd5 == '3'):
    code += "\n" + z
if (cmd5 == '4'):
    code += "\n" + w
if (cmd5 == '5'):
    code += "\n" + v
print(code)
print("")


# ejercicio 9

comando="13524"

cmd1=comando[0]
cmd2=comando[1]
cmd3=comando[2]
cmd4=comando[3]
cmd5=comando[4]
code=""
#                     1         2
#           01234567890123456789012345678
sentencias="buenas tardes dias noches bye"

x=sentencias[0:6]   # buenos
y=sentencias[7:13]  # dias
z=sentencias[14:18] # bye
w=sentencias[19:25] # tardes
v=sentencias[26:]   # noches

# Primer Bloque para el Codigo
if (cmd1 == '1'):
    code+=x
if (cmd1 == '2'):
    code+=y
if (cmd1 == '3'):
    code+=z
if(cmd1 =='4'):
    code+=w
if(cmd1 =='5'):
    code +=v
#2do bloque para el codigo
if (cmd2 == '1'):
    code += "\n" + x
if (cmd2 == '2'):
    code += "\n" + y
if (cmd2 == '3'):
    code += "\n" + z
if (cmd2 == '4'):
    code += "\n" + w
if (cmd2 == '5'):
    code += "\n" + v

# 3cer bloque para el codigo
if (cmd3 == '1'):
    code += "\n" + x
if (cmd3 == '2'):
    code += "\n"+ y
if (cmd3 == '3'):
    code += "\n" + z
if (cmd3 == '4'):
    code += "\n" + w
if (cmd3 == '5'):
    code += "\n" + v
# 4to bloque para el codigo
if (cmd4 == '1'):
    code += "\n" + x
if (cmd4 == '2'):
    code += "\n" + y
if (cmd4 == '3'):
    code += "\n" + z
if (cmd4 == '4'):
    code += "\n" + w
if (cmd4 == '5'):
    code += "\n" + v
# 5to bloque para el codigo
if (cmd5 == '1'):
    code += "\n" + x
if (cmd5 == '2'):
    code += "\n" + y
if (cmd5 == '3'):
    code += "\n" + z
if (cmd5 == '4'):
    code += "\n" + w
if (cmd5 == '5'):
    code += "\n" + v
print(code)
print("")


# ejercicio 10

comando="12345"

cmd1=comando[0]
cmd2=comando[1]
cmd3=comando[2]
cmd4=comando[3]
cmd5=comando[4]
code=""
#                     1
#           012345678901234
sentencias="f(X)=x+500"

x=sentencias[0:4]  # f(x)
y=sentencias[4:5]  # =
z=sentencias[5:6]  # x
w=sentencias[6:7]  # +
v=sentencias[7:]   # 500

# Primer Bloque para el Codigo
if (cmd1 == '1'):
    code+=x
if (cmd1 == '2'):
    code+=y
if (cmd1 == '3'):
    code+=z
if(cmd1 =='4'):
    code+=w
if(cmd1 =='5'):
    code +=v
#2do bloque para el codigo
if (cmd2 == '1'):
    code += "\n" + x
if (cmd2 == '2'):
    code += "\n" + y
if (cmd2 == '3'):
    code += "\n" + z
if (cmd2 == '4'):
    code += "\n" + w
if (cmd2 == '5'):
    code += "\n" + v

# 3cer bloque para el codigo
if (cmd3 == '1'):
    code += "\n" + x
if (cmd3 == '2'):
    code += "\n"+ y
if (cmd3 == '3'):
    code += "\n" + z
if (cmd3 == '4'):
    code += "\n" + w
if (cmd3 == '5'):
    code += "\n" + v
# 4to bloque para el codigo
if (cmd4 == '1'):
    code += "\n" + x
if (cmd4 == '2'):
    code += "\n" + y
if (cmd4 == '3'):
    code += "\n" + z
if (cmd4 == '4'):
    code += "\n" + w
if (cmd4 == '5'):
    code += "\n" + v
# 5to bloque para el codigo
if (cmd5 == '1'):
    code += "\n" + x
if (cmd5 == '2'):
    code += "\n" + y
if (cmd5 == '3'):
    code += "\n" + z
if (cmd5 == '4'):
    code += "\n" + w
if (cmd5 == '5'):
    code += "\n" + v
print(code)
print("")


# ejercicio 11

comando="12345"

cmd1=comando[0]
cmd2=comando[1]
cmd3=comando[2]
cmd4=comando[3]
cmd5=comando[4]
code=""
#                     1
#           01234567890123456789012345
sentencias="() int float input str"

x=sentencias[0:2]
y=sentencias[3:6]
z=sentencias[7:12]
w=sentencias[13:18]
v=sentencias[19:]

# Primer Bloque para el Codigo
if (cmd1 == '1'):
    code+=x
if (cmd1 == '2'):
    code+=y
if (cmd1 == '3'):
    code+=z
if(cmd1 =='4'):
    code+=w
if(cmd1 =='5'):
    code +=v
#2do bloque para el codigo
if (cmd2 == '1'):
    code += "\n" + x
if (cmd2 == '2'):
    code += "\n" + y
if (cmd2 == '3'):
    code += "\n" + z
if (cmd2 == '4'):
    code += "\n" + w
if (cmd2 == '5'):
    code += "\n" + v

# 3cer bloque para el codigo
if (cmd3 == '1'):
    code += "\n" + x
if (cmd3 == '2'):
    code += "\n"+ y
if (cmd3 == '3'):
    code += "\n" + z
if (cmd3 == '4'):
    code += "\n" + w
if (cmd3 == '5'):
    code += "\n" + v
# 4to bloque para el codigo
if (cmd4 == '1'):
    code += "\n" + x
if (cmd4 == '2'):
    code += "\n" + y
if (cmd4 == '3'):
    code += "\n" + z
if (cmd4 == '4'):
    code += "\n" + w
if (cmd4 == '5'):
    code += "\n" + v
# 5to bloque para el codigo
if (cmd5 == '1'):
    code += "\n" + x
if (cmd5 == '2'):
    code += "\n" + y
if (cmd5 == '3'):
    code += "\n" + z
if (cmd5 == '4'):
    code += "\n" + w
if (cmd5 == '5'):
    code += "\n" + v
print(code)
print("")

# ejercicio 13

comando="12345"

cmd1=comando[0]
cmd2=comando[1]
cmd3=comando[2]
cmd4=comando[3]
cmd5=comando[4]
code=""
#                     1
#           012345678901234
sentencias="200 + 300 = 500"

x=sentencias[0:3]
y=sentencias[4:5]
z=sentencias[6:9]
w=sentencias[10:11]
v=sentencias[12:]

# Primer Bloque para el Codigo
if (cmd1 == '1'):
    code+=x
if (cmd1 == '2'):
    code+=y
if (cmd1 == '3'):
    code+=z
if(cmd1 =='4'):
    code+=w
if(cmd1 =='5'):
    code +=v
#2do bloque para el codigo
if (cmd2 == '1'):
    code += "\n" + x
if (cmd2 == '2'):
    code += "\n" + y
if (cmd2 == '3'):
    code += "\n" + z
if (cmd2 == '4'):
    code += "\n" + w
if (cmd2 == '5'):
    code += "\n" + v

# 3cer bloque para el codigo
if (cmd3 == '1'):
    code += "\n" + x
if (cmd3 == '2'):
    code += "\n"+ y
if (cmd3 == '3'):
    code += "\n" + z
if (cmd3 == '4'):
    code += "\n" + w
if (cmd3 == '5'):
    code += "\n" + v
# 4to bloque para el codigo
if (cmd4 == '1'):
    code += "\n" + x
if (cmd4 == '2'):
    code += "\n" + y
if (cmd4 == '3'):
    code += "\n" + z
if (cmd4 == '4'):
    code += "\n" + w
if (cmd4 == '5'):
    code += "\n" + v
# 5to bloque para el codigo
if (cmd5 == '1'):
    code += "\n" + x
if (cmd5 == '2'):
    code += "\n" + y
if (cmd5 == '3'):
    code += "\n" + z
if (cmd5 == '4'):
    code += "\n" + w
if (cmd5 == '5'):
    code += "\n" + v
print(code)
print("")




# ejercicio 14

comando="54321"

cmd1=comando[0]
cmd2=comando[1]
cmd3=comando[2]
cmd4=comando[3]
cmd5=comando[4]
code=""
#                     1
#           0123456789012345678901234567890
sentencias="las aves con sin nido "

x=sentencias[0:3]
y=sentencias[4:8]
z=sentencias[9:12]
w=sentencias[13:16]
v=sentencias[17:]

# Primer Bloque para el Codigo
if (cmd1 == '1'):
    code+=x
if (cmd1 == '2'):
    code+=y
if (cmd1 == '3'):
    code+=z
if(cmd1 =='4'):
    code+=w
if(cmd1 =='5'):
    code +=v
#2do bloque para el codigo
if (cmd2 == '1'):
    code += "\n" + x
if (cmd2 == '2'):
    code += "\n" + y
if (cmd2 == '3'):
    code += "\n" + z
if (cmd2 == '4'):
    code += "\n" + w
if (cmd2 == '5'):
    code += "\n" + v

# 3cer bloque para el codigo
if (cmd3 == '1'):
    code += "\n" + x
if (cmd3 == '2'):
    code += "\n"+ y
if (cmd3 == '3'):
    code += "\n" + z
if (cmd3 == '4'):
    code += "\n" + w
if (cmd3 == '5'):
    code += "\n" + v
# 4to bloque para el codigo
if (cmd4 == '1'):
    code += "\n" + x
if (cmd4 == '2'):
    code += "\n" + y
if (cmd4 == '3'):
    code += "\n" + z
if (cmd4 == '4'):
    code += "\n" + w
if (cmd4 == '5'):
    code += "\n" + v
# 5to bloque para el codigo
if (cmd5 == '1'):
    code += "\n" + x
if (cmd5 == '2'):
    code += "\n" + y
if (cmd5 == '3'):
    code += "\n" + z
if (cmd5 == '4'):
    code += "\n" + w
if (cmd5 == '5'):
    code += "\n" + v
print(code)
print("")



# ejercicio 15
comando="32145"

cmd1=comando[0]
cmd2=comando[1]
cmd3=comando[2]
cmd4=comando[3]
cmd5=comando[4]
code=""
#                     1
#           0123456789012345678901234567
sentencias="no podras robar si llevas eso "

x=sentencias[0:9]
y=sentencias[14:9:-1]
z=sentencias[16:18]
w=sentencias[19:25]
v=sentencias[26::-1]

# Primer Bloque para el Codigo
if (cmd1 == '1'):
    code+=x
if (cmd1 == '2'):
    code+=y
if (cmd1 == '3'):
    code+=z
if(cmd1 =='4'):
    code+=w
if(cmd1 =='5'):
    code +=v
#2do bloque para el codigo
if (cmd2 == '1'):
    code += "\n" + x
if (cmd2 == '2'):
    code += "\n" + y
if (cmd2 == '3'):
    code += "\n" + z
if (cmd2 == '4'):
    code += "\n" + w
if (cmd2 == '5'):
    code += "\n" + v

# 3cer bloque para el codigo
if (cmd3 == '1'):
    code += "\n" + x
if (cmd3 == '2'):
    code += "\n"+ y
if (cmd3 == '3'):
    code += "\n" + z
if (cmd3 == '4'):
    code += "\n" + w
if (cmd3 == '5'):
    code += "\n" + v
# 4to bloque para el codigo
if (cmd4 == '1'):
    code += "\n" + x
if (cmd4 == '2'):
    code += "\n" + y
if (cmd4 == '3'):
    code += "\n" + z
if (cmd4 == '4'):
    code += "\n" + w
if (cmd4 == '5'):
    code += "\n" + v
# 5to bloque para el codigo
if (cmd5 == '1'):
    code += "\n" + x
if (cmd5 == '2'):
    code += "\n" + y
if (cmd5 == '3'):
    code += "\n" + z
if (cmd5 == '4'):
    code += "\n" + w
if (cmd5 == '5'):
    code += "\n" + v
print(code)
print("")
# FIN_BUSQUEDA