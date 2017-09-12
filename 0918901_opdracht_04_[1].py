# Naam:     Reuben Domacasse
# Stunr:    0918901
# Klas:     ICTVT1C
# Datum:    12-09-2017

#Opdracht 4
#Klanten kunnen ook in maandelijkse termijnen betalen. Als jaarrente rekenen wij 11.2%.
#Bereken wat de maandrente bedraagt voor de klanten

import math
y = 11.2
formule = math.pow(1+(11.2/100),y)
maandrente = ((formule)-1)*100
x = ("{0:.3f}".format(float(maandrente)))

print "De maandrente bedraagt "+format(x)+" bij een jaarrente van "+format(y)+"%."