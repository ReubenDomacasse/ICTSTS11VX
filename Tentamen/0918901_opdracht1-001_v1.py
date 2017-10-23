# Tentamen versie   :BMFWRDZN
# Gegevens          :Reuben Domacasse 0918901 23-10-2017
# Opgave            :1-001

# Inleiding:    De inhoud van een voorwerp met een diameter van 33 cm wordt berekend met de formule: 1/8 x 3,14 x (33^4) / 5
# Opdracht:     Schrijf een programma dat deze berekening uitvoert.
# Eisen:        Vervang de getallen door variabelen.
#               De uitkomst wordt op het scherm geprint met de zin: "De inhoud van de bol is x kubieke cm"
#               Waarbij x de uitkomst is van de berekening

# Programma:    DIAMETER BEREKENEN

#defineer variable pi
pi          = float(3.14)
#defineer variable diameter
diameter    = (33**4)/5
#defineer variable hoogte
hoogte      = 1/8
#defineer variable x
x           = str(float(hoogte*pi*diameter))

#print het resultaat van de formule met variable x
print ("De inhoud van de bol is "+x+" kubieke cm.")