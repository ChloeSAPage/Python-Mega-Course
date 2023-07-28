def get_average():
    with open ("files/data.txt", "r") as file:
        data = file.readlines()
    values = data[1:]
    values = [float(value) for value in values]

    average_local = sum(values) / len(values)
    return average_local
    

average = get_average()
print(f"this is the average {average}")



