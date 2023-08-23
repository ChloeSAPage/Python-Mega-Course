filenames = ["1. Raw Data.txt", "2. Reports.txt", "3. Presentations.txt"]

for filename in filenames:
    filename = filename.replace(".", "-" , 1)
    print(filename)

tuple_example = ("1. Raw Data.txt", "2. Reports.txt", "3. Presentations.txt") #tuple is unchangeable, unlike a list. e.g not ammendable
print(type(tuple_example))


