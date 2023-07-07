def main():
    userInput = input("Item: ")
    
    fruits = {
        "Apple": 130, 
        "Avocado": 50,
        "Banana": 110,
        "Cantaloupe": 50,
        "Grapefruit": 60,
        "Grapes": 90,
        "HoneydewMelon": 50,
        "Kiwifruit": 90,
        "Lemon": 15,
        "Lime": 20,
        "Nectarine": 60,
        "Peach": 60,
        "Orange": 80,
        "Pear": 100,
        "Pineapple": 50,
        "Plums": 70,
        "Strawberries": 50,
        "SweetCherries": 100,
        "Tangerine": 50,
        "Watermelon": 80
    }

    print(f"Calories: {fruits[userInput]}")

main()