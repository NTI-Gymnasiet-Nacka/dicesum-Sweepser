# Dice sum probability calculator
# Författare:
# Datum:

def main():
    
    max_value1=10
    max_value2=10

   
    total = {} 

   
    for i in range(1, max_value1 + 1):
        for j in range(1, max_value2 + 1):
            summa = i + j
            if summa in total:
                total[summa] += 1 
            else:
                total[summa] = 1

    max_frequency = max(total.values()) 
    
    summorna = []
    for summa, x in total.items(): 
        
        if x == max_frequency:
            summorna.append(summa)


    print("Den mest sannolika summan/summorna är:", summorna)

if __name__ == "__main__":
    main()
