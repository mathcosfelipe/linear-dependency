from os import remove


def verify_vectors(vectors):

    characters = []

    for i in vectors:
        characters.append(i)

    pipe = False

    if '|' in characters:
        pipe = True
    
    array_vectors = []

    for j in vectors:
        


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
            vectors = input("Inform the vectors. For example: (1;3)|(4;8). Use | for separate the vectors: ")
        except:
            print("Error. Try again!")
        else:
            if verify_vectors(vectors) == False:
                print("Invalid input. Try again.")
            else:
                break

main()