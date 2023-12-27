from string import ascii_uppercase,ascii_lowercase,digits,punctuation
from random import shuffle,choice
from os import getcwd


def password_generator(length=8):
    list_of_chars = list(ascii_lowercase+ascii_uppercase+digits+punctuation)
    password = ""
    for i in range(length):
        shuffle(list_of_chars)
        password += choice(list_of_chars)
    else:
        del list_of_chars
        return password


def main():
    try:
        pass_len = int(input("Enter the length of the password you want:- "))
        
        match input("Do you want to record password in txt file? (y/n): ").lower():
            case "y":
                social_media = input("For which social media you want to set password (Ex:- Google,Instagram,Twitter etc.):- ")
                print("\n\n")
                
                password = password_generator(pass_len)
                with open("password.txt","a") as f:
                    f.write(f"{social_media}:- {password}\n")
                
                print(f"Your Password is: {password}")
                print(rf"Your Password is stored in {getcwd()}\password.txt")
                
                del password
            case "n":
                print(password_generator(pass_len))
                
            case _:
                print("Please give response in y/n")
    except:
        print("Please Input a Number")


if __name__ =="__main__":
    main()
    