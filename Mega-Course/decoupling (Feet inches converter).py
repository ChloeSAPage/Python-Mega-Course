import converters

feet_inches = input("enter feet and inches ")


parsed = converters.parse(feet_inches)
result = converters.convert(parsed['feet'], parsed['inches'])

print(f"{parsed['feet']} feet and {parsed['inches']} is equal to {result}")

if result < 1:
    print("Too small to ride")

else:
    print("You can ride")