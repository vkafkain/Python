def main():
    question = input("What is the Answer to the Great Question of Life, the Universe, and Everything?")
    correct = "Yes"
    incorrect = "No"
    if question == "42" or question == "forty-two" or question == "forty two":
        print(correct)
    else:
        print(incorrect)


main()