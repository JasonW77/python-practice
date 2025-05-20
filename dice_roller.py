import random

def roll_dice(num_dice, num_sides):
    results = []
    for _ in range(num_dice):
        result = random.randint(1, num_sides)
        results.append(result)
    return results

def main():
    print("🎲 Dice Roller App 🎲")
    while True:
        try:
            num_dice = int(input("How many dice would you like to roll? "))
            num_sides = int(input("How many sides per die? (e.g. 6 for standard) "))
            if num_dice < 1 or num_sides < 2:
                print("Please enter valid positive numbers.")
                continue
            rolls = roll_dice(num_dice, num_sides)
            print(f"Results: {rolls}")
        except ValueError:
            print("⚠️ Invalid input. Please enter whole numbers.")
            continue
        
        again = input("Roll again? (y/n): ").lower()
        if again != "y":
            print("👋 Thanks for rolling!")
            break

if __name__ == "__main__":
    main()