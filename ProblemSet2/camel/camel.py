def main():
     
    camel = input("camelCase: ")
    print("snake_case: ", end="")

    for letter in camel:
      
        if letter.isupper():
            print("_" + letter.lower(), end="") 
        else:
            print(letter, end="") 

main()