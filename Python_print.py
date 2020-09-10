a = True

while a:
	hello = "Hello, my name is {owner}. What's yours?\n"
	print(hello.format(owner = "Joost"))
	
	username = input("My name is:")
	print("Hello " + username, "!")
	
	question = input("Would you like to know the date?\n")
	if question == "yes":
		import datetime
		import time
		
		x = datetime.datetime.now()
		
		print("Today is the " +  x.strftime("%d"), "of " + x.strftime("%B"), ".")
	
	
	test2 = input("Wil je dit gesprek nog een keer voeren? yes/no\n")
	if test2 == "yes":
		continue
	
	a = False
	print("Het programma stopt nu, tot de volgende keer!")
	time.sleep(2)
	exit