def main():

    vocals = ("a", "e", "i", "o", "u")

    phrase = input("Input: ")

    for letter in vocals:
        phrase = phrase.replace(letter, "")

    print(f"Output: {phrase}") 

main()