import random
v1 = "Hoe is het met jouw ? "
while True:
    print(v1)
    ant = input()
    if ant == "goed":
        print("Mooi zo ")
        break
    elif ant == "Slecht":
        
        print("Wil je er over praten ?")
        print("a. Ja")
        print("b. Nee")
        ant = input()
        if ant == "a":
                print("wat is er ?  ")
                print("a.Ik heb het moeilijk met iets ")
                print("b.Laat maar ")
                ant = input()
                if ant == "a":
                    print("Oh jammer vertel ( je kan geen eigen mening zetten omdat mijn progammeur niet in staat is om een open antwoord in dit verhaal te zetten")
                    print("Laat maar  ")
                    print("Ik zit het even niet zitten met mijn leven")
                    input()
                    break
                if ant == "b":
                    print("Oh jee ik wil dat je contact zoekt met iemand met wie je kan gaan praten over je probleem ")
                    print("Nee")
                    input()
                    break
           