import random
import requests

ANSI_YELLOW = "\033[1;33m"
ANSI_GREEN =  "\033[1;32m"
ANSI_RESET =  "\033[m"
WORDLIST_URL = "https://gist.githubusercontent.com/cfreshman/a7b776506c73284511034e63af1017ee/raw/60531ab531c4db602dacaa4f6c0ebf2590b123da/wordle-nyt-answers-alphabetical.txt"

def main():
    try:
        with open("words.txt", "r") as f:
            words = f.read().split("\n")
    except FileNotFoundError:
        print("downloading file...")
        r = requests.get(WORDLIST_URL)
        with open("words.txt", "w") as f:
            f.write(r.text)
        words = r.text.split("\n")
        print("Done")
    
    while True:
        word = random.choice(words)
        tries_left = 6
        won = False
        inp = ""
        while tries_left:
            while not len(inp) == 5:
                inp = input().lower()
            
            for i, c in enumerate(inp):
                if inp == word:
                    won = True
                    break
                elif word[i] == c:
                    print(ANSI_GREEN, end="")
                elif c in word:
                    print(ANSI_YELLOW, end="")
                print(c + ANSI_RESET, end="")
            if won:
                break
            print("")
            inp = ""
            tries_left -= 1
        if won:
            print(f"Congrats you won (with {tries_left} tries left)...")
        else:
            print(f"you lost the word was {word}...")
        if input("Do you want to play again [Y/n]: ").lower() != "y":
            break

if __name__=="__main__":
    main()