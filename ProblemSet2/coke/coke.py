def main():
    
    total_prize = 50
    while True:
        print(f"Amount Due: {total_prize}")

        coins = int(input("Insert Coin:"))
        total_prize = total_prize - coins
        
        if total_prize > 0:
            continue
        else:
            print(f"Change Owed: {total_prize}")
            break

main()