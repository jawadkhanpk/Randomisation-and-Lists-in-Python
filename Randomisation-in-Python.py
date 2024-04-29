import random

# Random Integer
random_integer = random.randint(1,10)
print(random_integer)

# Random Float, this will generate random number from 0.00.... to 0.99....
random_float = random.random()
print(random_float)

# Random Float, this will generate random number from 0.00.... to 9.99....
random_float_mul = random.random() * 10
print(random_float_mul)