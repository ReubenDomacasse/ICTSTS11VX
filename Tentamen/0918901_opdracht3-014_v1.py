# Tentamen versie   :BMFWRDZN
# Gegevens          :Reuben Domacasse 0918901 23-10-2017
# Opgave            :3-014

# Opdracht      : Schijf een programma die aan de volgende voorwaarden voldoet.
# Eisen         : De gebruiker mag een getal in vullen tussen 0 en 999.
#               : Print het getal uit als het tussen de 1 en 250 zit.
#               : Print het getal uit als het tussen de 251 en 340 zit.
#               : Print voor elk ander getal buiten 1 en 340 een melding dat het getal buiten de gedefineerde range valt.
#               : Als het ingevoerde getal niet voldoet aan de eis van 0 tot 999 geef een foutmelding aan.

# Programma     : INPUT RANGE CONTROL

print("Vul een getal in tussen de 0 en de 999")
getal = int(input())
if (getal > 1 and getal < 250):
    print("Het getal is tussen de 1 en de 250")
elif (getal > 251 and getal < 340):
    print("Het getal is tussen de 251 en de 340")
else:
    print("Het getal valt buiten de gedefineerde range")