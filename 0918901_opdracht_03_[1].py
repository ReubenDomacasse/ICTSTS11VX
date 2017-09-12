# Naam:     Reuben Domacasse
# Stunr:    0918901
# Klas:     ICTVT1C
# Datum:    12-09-2017

#Opdracht 3
#Schrijf een programma dat de kosten van de zakelijke directie telefoons berekent
#Ze hebben een 2-jarig contract.
#Totale maandkosten = kosten Jacob + kosten Fred
#Kosten contractduur = 2 * 12 * totale maandkosten

Jacob_abonnement    = float(45)
Jacob_verzekering   = float(35)
Jacob_bellensms     = float(15)

Fred_abonnement     = float(48.50)
Fred_verzekering    = float(38.75)
Fred_bellensms      = float(15)

Jacob_kosten        = Jacob_abonnement + Jacob_verzekering + Jacob_bellensms
Fred_kosten         = Fred_abonnement + Fred_verzekering + Fred_bellensms

Maand_kosten        = Jacob_kosten + Fred_kosten
Contractduur        = format(2*12*Maand_kosten)

print "De totale kosten van de directie telefoons gedurende het contract bedraagt "+Contractduur+" euro."