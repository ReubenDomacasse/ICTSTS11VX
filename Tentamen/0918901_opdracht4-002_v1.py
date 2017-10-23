# Tentamen versie   :BMFWRDZN
# Gegevens          :Reuben Domacasse 0918901 23-10-2017
# Opgave            :4-002

# Opdracht      : schrijf een programma dat 200 random getallen tussen de 10 en de 1000 print.
# Eisen         : De volgende tekst wordt op het scherm geprint: Een willekurig getal:
#               : 200 random getallen
#               : als het getal 100 wordt gekozen wordt het programma gestop.

# Programma     : RANDOM STOPWATCH
import random

for x in range(200):
    willekurig_getal = random.randint(10,100)
    print(str(x) + "\tEen willekurig getal:" + str(willekurig_getal))
    if(willekurig_getal == 100):
        break
    else:
        continue