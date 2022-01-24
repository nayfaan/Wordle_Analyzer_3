def run():
    with open("./input/all_words-saine.txt", "rt") as f:
        sol_saine = f.read().splitlines()
    
    sol_sans_saine = []
    
    for word in sol_saine:
        if len(set(word) & set("saine")) == 0:
            sol_sans_saine.append(word)
    
    sol_sans_saine.sort()
    
    for x in sol_sans_saine:
        print(x)
    

if __name__ == "__main__":
    
    run()