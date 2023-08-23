date = input("Enter todays date: ")
mood = input("Rate your mood from 1 - 10: ")
thoughts = input("Tell me about your day: \n")

with open(f"{date}.txt", "w") as file:
    file.write(mood + 2 * "\n")
    file.write(thoughts)
    
