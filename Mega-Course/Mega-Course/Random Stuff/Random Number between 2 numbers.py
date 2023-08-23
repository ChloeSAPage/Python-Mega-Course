import random

user_lower_bound = int(input("Enter the lower bound "))
user_upper_bound = int(input("Enter the upper bound "))

random_number = random.randint(user_lower_bound, user_upper_bound)
print(random_number)