# Dice sum probability calculator
# Författare:
# Datum:

def main():
    
    max_value1=10
    max_value2=10

   
    total = {} # Sparar värderna

   
    for i in range(1, max_value1 + 1):
        for j in range(1, max_value2 + 1):
            summa = i + j
            if summa in total:
                total[summa] += 1 # Sparar värdena i total
            else:
                total[summa] = 1

    max_frequency = max(total.values()) # Tar alla som har störst värde
    
    summorna = []
    for summa, x in total.items(): # Går igenom allt och tar fram dom som har samm värde
        
        if x == max_frequency:
            summorna.append(summa)


    print("Den mest sannolika summan/summorna är:", summorna)

if __name__ == "__main__":
    main()
