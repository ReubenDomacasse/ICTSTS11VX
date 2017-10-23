# Tentamen versie   :BMFWRDZN
# Gegevens          :Reuben Domacasse 0918901 23-10-2017
# Opgave            :2-005

# Inleiding     : De omtrek van een rechthoek kan worden berekennd met de formule: 2 * zijde A + 2 * zijde B
# Opdracht      : Schrijf een programa dat de omtrek berekend
# Eisen         : Vraag de gebruiker naar de getallen A & B.
#                 Voor A mag er alleen gekozen worden voor 10,20, 30 of 40.
#                 Alle getallen zijn het datatype float.
#                 Een melding geven als het gegeven getal voor B kleiner is dan 1.
#                 De omtrek wordt berekend.
#                 De omtrek wordt op het scherm en in de GUI weergegeven.

# Programma     : OMTREK BEREKENEN
import easygui

welkomsbericht  = easygui.msgbox ("Goedendag,\nDe omtrek van een rechthoek \nkan worden berekennd met de \nformule: 2 * zijde A + 2 * zijde B")
overzijde = float(2.0)

while(True):
    input_a_zijde = easygui.enterbox("Vul een getal in voor zijde A\nKies uit: 10, 20, 30, 40")
    if (input_a_zijde == '10' or input_a_zijde == '20' or input_a_zijde == '30' or input_a_zijde == '40'):
        a_zijde = float(input_a_zijde)
        print("Zijde A:\t" + str(a_zijde))
        input_b_zijde = easygui.enterbox("Vul een getal in voor zijde B\n Let op! het getal mag niet kleiner zijn dan 1")
        if (float(input_b_zijde) > 1.0):
            b_zijde = float(input_b_zijde)
            print("Zijde B:\t" + str(float(b_zijde)))
            omtrek_formule = overzijde * a_zijde + overzijde * b_zijde
            omtrek = float(omtrek_formule)
            print("Formule:\t" + str(float(overzijde * a_zijde + overzijde * b_zijde)))
            print("De omtrek van een rechthoek is:\t" + str(float(omtrek)))
            berekening = easygui.msgbox("De omtrek van een rechthoek is:\t" + str(omtrek))
        else:
            print("verkeerde input: "+input_b_zijde)
            fout = easygui.msgbox("Het ingevoerde getal is kleiner dan 1 probeer opnieuw!")

    else:
        print("verkeerde input: "+ input_a_zijde)
        fout = easygui.msgbox("Het ingevoerde getal is onjuist probeer opnieuw!")


