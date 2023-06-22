def main():
    question = input("Greetings: ")
    responseHello = "Hello"
    if responseHello in question:
        print("$0")
    elif question.startswith('H'):
        print("$20") 
    else:
        print("$100") 

main()