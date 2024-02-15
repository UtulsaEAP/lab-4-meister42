"""
Complete the following python code to print the password entered by the user with the modifications described in the readme

i becomes 1
a becomes @
m becomes M
B becomes 8
s becomes $

Name: Henry Holman
Lab Time: Thursday 2 Pm
"""

def password_mod():
    word = input()
    password = ""
    for letter in word: 
        if letter == "i" :
            password = password + "1" 
        elif letter == "a" :
            password = password + "@"
        elif letter == "m" :
            password = password + "M"
        elif letter == "B" :
            password = password + "8"
        elif letter == "s" :
            password = password + "$"
        else:
            password = password + letter
    password = password + "!"
    print(password)
    # Type your code here.

if __name__ == "__main__":
    password_mod()