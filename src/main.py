def verify_vectors(vectors, domain):

    characters = []

    for i in vectors:
        characters.append(i)

    if '|' in characters:
        return True
    else:
        return False
    
    print(i)
    # array_vectors = []

    # for j in vectors:
        # print(j)
        


def main():

    while True:
        try:
            domain = int(input("Inform the domain set: "))
        except:
            print("Error. The domain is a integer number. Example: 2, that means R2. Try again.")
        else:
            break

    while True:
        try:
            # vectors = input("Inform the vectors. For example: (1;3)|(4;8). Use | for separate the vectors: ")
            vectors = "(1;2)|(7;9)"
        except:
            print("Error. Try again!")
        else:
            if verify_vectors(vectors, domain) == False:
                print("Invalid input. Try again.")
            else:
                break

    # response = 

main()