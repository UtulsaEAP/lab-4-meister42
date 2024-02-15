"""
Complete the following python code to reverse the string entered by the user.

Name: Henry Holman
Lab Time: Thursday @ 2pm
"""

def reverse_string():
    # YOUR CODE HERE
    string = str(input())
    rev = ""
    while string not in ["d", "done", "Done"]:
        rev = ""
        for letter in string:
            rev = letter + rev
        print(rev)
        string = str(input())

if __name__ == "__main__":
    reverse_string()