import random

random_number = random.randrange(0,5)
print(random_number)

random_number = random.random() * 100  # * by 100 to convert the generated random number in range 0 to 100

print(random_number)

ls = ["satarplus", "DD1", "Zee tv", "Hungama", "zee cinema", "star gold"]

random_item = random.choice(ls)
print(random_item)

