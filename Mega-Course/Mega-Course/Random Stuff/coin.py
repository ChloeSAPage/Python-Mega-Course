while True:
    with open("coin.txt", "r") as file:
        lines = file.readlines()
        total = int(lines[0])
        heads = int(lines[1])
        tails = int(lines[2])

    coin =  input("Throw the coin and enter heads or tails here: ? ")
      
    match coin:
        case "heads":
            total += 1
            heads += 1
                        
        case "tails":
            total += 1
            tails += 1
            
        case _:
            print("Invalid Input")
            continue
        
    percentage_heads = (heads / total)  * 100
    print(f"Heads: {percentage_heads}%")
    with open("coin.txt", "w") as file:
            file.write(str(total) + "\n")
            file.write(str(heads) + "\n")
            file.write(str(tails) + "\n")     

    
        
        