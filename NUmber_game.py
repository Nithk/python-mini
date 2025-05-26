import random

def game(high):
    print("hello gamer ")
    print("ready to play game ")

    num = random.randint(1, 20)
   
    print("I'M picking a number, try to guess it!!!")
    print("Hint: number between 1 to 20")
    
    at = 0
    while at < 6:
        print(f"you have {6 - at} attempts to go")
        print(f"let's make guess no {at + 1}:", end="")
        
        try:
            g = int(input())
        except ValueError:
            print("Please enter a valid number.")
            continue

        at += 1

        if g == num:
            print("you nailed it broo")
            if at < high:
                high = at
            break
        elif g > num:
            print("your guess is too high")
        else:
            print("your guess is too low")

    with open("scores.txt", 'w') as f:
        f.write(str(high))
    print(f"your high score is {high}")

# --- Main Program Logic ---
try:
    with open("scores.txt", 'r') as f:
        con = f.read().strip()
        if con == "didn't play till now":
            high = 6
            print("you didn't play this before")
        else:
            high = int(con)
            print("you once guessed in", high, "attempts only")
except FileNotFoundError:
    print("file not found ⚠️. Creating new high score file.")
    high = 6

# Call the game with the high score
game(high)
