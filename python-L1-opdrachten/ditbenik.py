print("Hello You!")
print("Ik ben Uday")
print("Wie ben jij?")
x = input("Typ je naam in:")
print("hello " + x)

print("Ik ben (g)een nieuwkomer op het Mediacollege Amsterdam, door vragen te  beantwoorden die over mij gaan kan je me beter leren kennen ! , als je genoeg vragen  goed hebt ken je me heel goed !, maar als je veel fouten maakt restart de quiz voledig en is het beter dat je dit opnieuw doet na dat je me wat beter leert kennen :) SUCCES !.")

fouten = 0
# Vraag 1
answer1 = input("voor ik naar het MBO op het Mediacollege Amsterdam kwam studeerde ik op de Middelbaren school, welke school ? \n a. CallandLyceum \n b. Wellantcollege \n c. Huygens \nAnswer: ")
if answer1 == "b" or answer1 == "Wellantcollege":   
    print ("goed!")
    print("\n")
else:
    print("Fout! het juiste antwoord is Wellantcollege.")
    fouten = fouten + 1
    print("\n")
# Vraag 2
answer2 = input("welke opleiding in het HBO  wil ik doen na deze MBO opleiding ? \n a. geen \n b. Software enginering \n c. Etische Hacker \nAnswer: ")
if answer2 == "b" or answer2 == "Software enginering":   
    print ("goed!")
    print("\n")
else:
    print("Fout! het juiste antwoord is Software enginering .")
    
    print("\n")
# Vraag 3 
answer3 = input("ben ik ooit in mijn hele leven tot nu toe blijven zitten  ? \n a. JA \n b. Weet ik niet  \n c. Nee  \nAnswer: ")
if answer3 == "c" or answer3 == "Nee":   
    print ("goed!, ik ben wel een goeie jongen he !")
    print("\n")
else:
    print("Fout! Ik ben wel 1 keer uit de klas gestuurd maar dat is een verhaal voor de andere keer :).")
    
    print("\n")
# Vraag 4
answer4 = input("Hou ik van stilte  ? \n a. Nee \n b. Ja \nAnswer: ")
if answer4 == "b" or answer4 == "Ja":   
    print ("goed!")
    print("\n")
else:
    print("Fout! het juiste antwoord is Ja.")
    
    print("\n")



print("Je hebt ",fouten,"fouten gemaakt")
while True:
    if fouten == 3:
        print("Let's try again")
        print("Je hebt teveel fouten gemaakt dus jij krijgt meer vragen en als je die goed beantwoord ben je klaar"
        
    else:
        if fouten == 0:
            print("hoera you won.")
            quit()


# Vraag 5
answer5 = input("Rook ik  ? \n a. Ja \n b. Nee \nAnswer: ")
if answer5 == "b" or answer5 == "Ja":   
    print ("goed!")
    print("\n")
else:
    print("Fout! het juiste antwoord is Ja.")
    
    print("\n")
# Laatste bericht !
print("goed gedaan!,je hebt het einde van de quiz behaald en alle vragen beantwoord! bedankt voor het spelen")

