####
#              10
#     012345678901
msg="HOLA ANTONIO"
print(msg[::-1]) ### muestra la cadena  "OINOTNA ALOH"

###
#               10        20        30       40
#    01234567890123456789012345678901234567890
msg="ESCUELA PROFESIONAL INGENERIA ELECTRONICA"
print(msg[29:41]) ### muestra la cadena "ELECTRONICA"
print(msg[8:14]) ### muestra la cadena "PROFES"
print(msg[5:13]) ### muestra la cadena "LA PROFE"

###
#               10        20        30       40
#    012345678901234567890123456789012345678901234567
msg="ORGANIZACION DE LA INVASION Y CONQUISTA DEL PERU"
print(msg[0:8]) ### muestra la cadena "ORGANIZA"
print(msg[::-3]) ### muestra la cadena "UPEAIN NSNAENCING"
print(msg[::+5]) ### muestra la cadena "OIO NOCIDE"

###
#               10        20        30
#    012345678901234567890123456789
msg="SODA STEREO: DE MUSICA LIGUERA"
print(msg[5:-5]) ### muestra la cadena " STEREO: DE MUSICA LI"
print(msg[::10]) ### muestra la cadena "SOC"
print(msg[-4:-1]) ### muestra la cadena "UER

###
#               10        20       30       40
#    0123456789012345678901234567890123456790123
msg="SERA QUE SOS UN ANGEL Y NO PODES DISIMULAR"
print(msg[-4:+1]) ### muestra la cadena VACIA
print(msg[-9::+1]) ### muestra la cadena "DISIMULAR"
print(msg[:1]) ### muestra la cadena "S"

###
#              10        20       30       40
#    012345678901234567890123456789012345679012345
msg="HOY ME LEVANTE CON GANAS DE VOLVERTE ENAMORAR"
print(msg[:]) ### muestra la cadena "HOY ME LEVANTE CON GANAS DE VOLVERTE ENAMORAR"
print(msg[4:24]) ### muestra la cadena "HOY ME LEVANTE CON GANAS DE VOLVERTE ENAMORAR"
