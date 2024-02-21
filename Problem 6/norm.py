"""
Complete the following python code to take in a list of values from the user and then normalize them

Name: Henry Holman
Lab Time: Thursday 2pm
"""

def norm():
    # Write your code here
    floatnum = int(input())
    numbers = []
    for i in range(1, floatnum + 1):
        num = float(input())
        numbers.append(num)
    maxvalue = float(max(numbers))
    outputnumbers =  [i/maxvalue for i in numbers]
    for i in range (1, floatnum + 1 ):
        print(f'{outputnumbers[i-1]:.2f}')
    
# 5","30.0","50.0","10.0","100.0","65.0"
if __name__ == "__main__":
    norm()