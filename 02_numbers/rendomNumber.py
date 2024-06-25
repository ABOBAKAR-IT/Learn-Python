import random
print(random.random()) # return random value from 0 to 1

print(random.randint(1,100))

print(random.randrange(1,100))

list = [1,2,3,4,5,6,7,8,9,10]

print(random.choice(list)) # return one random value from list

print(random.choices(list)) # return one random length list

mylist = ["apple", "banana", "cherry"]

print(random.choices(mylist, weights = [10, 1, 1], k = 14))


random.shuffle(list) # change the list random order
print(list)

