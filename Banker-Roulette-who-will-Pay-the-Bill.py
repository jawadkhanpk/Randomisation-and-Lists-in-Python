import random
name_string = input("Give me everybody's names separated by comma: ")
names = name_string.split(", ")

number_items = len(names)

choice = random.randint(0, number_items - 1)
# added -1 because list index starts from 0
person_who_will_pay = names[choice]
print(person_who_will_pay + " is gonna buy meal today!")


#simple way, while using random.choice functionally can skip code from line 5-10
# person_who_will_pay = random.choice(names)
# print(person_who_will_pay + " is gonna buy meal today!")
