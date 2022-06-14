import sys
import math


def factorial(str):
    try:
        n=int(str)
        return math.factorial(n)
    except Exception as ex:
        print(f"Error: {ex}")
        
if __name__ == "__main__":
    print(factorial(sys.argv[1]))
    

        