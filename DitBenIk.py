import time
a = True
while a:
	print("Hello You!")
	print("Ik ben Joost.")
	
	time.sleep(1)
	
	q1 = input("Wie ben jij?\n")
	print("Hallo " + q1, "!")
	
	print("Ik ben een nieuwkomer op het Mediacollege Amsterdam en ik zoou het graag over wat leuke dingen willen hebben, \n")
	print("Ik heb wat onderdelen voorbereid, jij mag kiezen!")
	time.sleep(3)
	print("Wat wil je over mij weten?\n")
	
	print("(1) Hobby's!")
	print("(2) Vrienden!")
	print("(3) Je vorige school!\n")
	
	q2 = input("Kies uit 1, 2 of 3.\n")
	if q2 == "1":
		print("Mijn hobby's zijn: gamen, chillen met de jongens en onder andere Virtual Reality activiteit!")
	if q2 == "2":
		print("Ik ben bevriend met 5 jongens rond mijn leeftijd:\n Jaro, Wouter, Giel en Ruben, dit zijn echt goede vrienden en we gamen vaak!")
	if q2 == "3":
		print("Ik heb hiervoor op het Regius College in schagen gezeten,\nIk woon dan ook in Anna Pauwlona ookal heb ik voor de langste tijd in Wieringerwaard gewoont,\n ik ben 3 maanden geleden verhuisd van Wieringerwaard naar Anna pauwlona.")
	time.sleep(2.5)
	
	q2 = input("Kies uit 1, 2 of 3.\n")
	if q2 == "1":
		print("Mijn hobby's zijn: gamen, chillen met de jongens en onder andere Virtual Reality activiteit!")
	if q2 == "2":
		print("Ik ben bevriend met 5 jongens rond mijn leeftijd:\n Jaro, Wouter, Giel en Ruben, dit zijn echt goede vrienden en we gamen vaak!")
	if q2 == "3":
		print("Ik heb hiervoor op het Regius College in schagen gezeten,\nIk woon dan ook in Anna Pauwlona ookal heb ik voor de langste tijd in Wieringerwaard gewoont,\n ik ben 3 maanden geleden verhuisd van Wieringerwaard naar Anna pauwlona.")
	time.sleep(2.5)
	
	q2 = input("Kies uit 1, 2 of 3.\n")
	if q2 == "1":
		print("Mijn hobby's zijn: gamen, chillen met de jongens en onder andere Virtual Reality activiteit!")
	if q2 == "2":
		print("Ik ben bevriend met 5 jongens rond mijn leeftijd:\n Jaro, Wouter, Giel en Ruben, dit zijn echt goede vrienden en we gamen vaak!")
	if q2 == "3":
		print("Ik heb hiervoor op het Regius College in schagen gezeten,\nIk woon dan ook in Anna Pauwlona ookal heb ik voor de langste tijd in Wieringerwaard gewoont,\n ik ben 3 maanden geleden verhuisd van Wieringerwaard naar Anna pauwlona.")
	time.sleep(2.5)
	a = False

print("Nou dat was leuk, misschien wil je het gesprek opnieuw voeren,\nzo ja zeg het dan maar!")
b = True
while b:
	q3 = input("Ja of Nee?\n")
	if q3 == "Ja":
		b = False
		a = True
		continue
	if q3 == "Nee":
		print("Oke, je hebt vast andere dingen te doen,\nTot de volgende keer!")
		time.sleep(2)
		b = False
	else:
		print("Dit is geen goed antwoord probeer het nog een keer.\n")
		continue
exit