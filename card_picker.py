import random

welcome = "This is 'Random Card Picker' program."
print (welcome.center(75))

names_string = str(input("Give me everybody's name seperated by comma and space: "))
names = names_string.split(", ")

total_person = len(names)
random.choice = random.randint(0, total_person-1)

rich_guy = names[random.choice]
print(f"{rich_guy} is going to pay for the dinner.")