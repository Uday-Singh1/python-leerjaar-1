print("je wekker gaat af en je eerste les  begint om 9 uur, sta je op of slaap je door ?")
choice = input()
if choice == 'sta op':
    print("je staat op met veel slaap, maar je gaat naar school en hebt ook belangerijken informatie gehoord voor school en de dag ging over het algemeen snel dus je kan thuis weer lekker uitslapen")
if choice == 'doorslapen':
    print("Hmmmmmm zzzzzzzzzzzzzzzzzzzzzzzzzz")
else:
     choice = input()
print("oh nee je hebt je te erg verslapen het is al 8:45 uur ! ,  meld je je ziek of ga je gewoon naar school ?")
choice = input()
if choice == 'ziekmelden':
    print("je meld je ziek maar je mist belangerijken informatie over de komende tijd !")
elif choice == 'naar school gaan ':
    print("je gaat naar school en wordt gemeld as te laat maar je hoort wel belangerijken informatie die je nodig hebt voor de komende tijd ")
else:
    print(choice, " wasn't a valid choice")
