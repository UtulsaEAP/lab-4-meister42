"""
Complete the following python code to print the reverse binary representation of positive integer number entered by the user.

Name: Henry Holman
Lab Time: Thursday @ 2pm

"""


def reverse_binary():


    user_num = int(input())
    output = ""
    while user_num > 0:
        binary = user_num % 2
        user_num = int(user_num/2)
        output += str(binary)
    print(str(output))

if __name__ == "__main__":
    reverse_binary()