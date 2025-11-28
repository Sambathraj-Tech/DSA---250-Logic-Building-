==============================================================================================================================================================

      LEVEL - 1 : Simple Conditions (10 Problems)

==============================================================================================================================================================
1. Take a number and print whether its Positive or Negative or zero

def solution(n):
    if n == 0:
        print("Its zero number.")
    elif n < 0:
        print("Its negative number.")
    elif n > 0:
        print("Its positive number.")
if __name__ == '__main__':
    n = 0
    solution(n)
==============================================================================================================================================================
2. Check if a number is even or odd

def solution(n):
    if n % 2 == 0:
        print("Even  number.")
    else:
        print("Odd number.")
if __name__ == '__main__':
    n = 0
    solution(n)
==============================================================================================================================================================
3. Check if a number is divisble by 5.

def solution(n):
    if n % 5 == 0:
        return f"{n} is divisible by 5"
    return f"{n} is not divisible by 5"

if __name__ == '__main__':
    n = 6
    print(solution(n))
==============================================================================================================================================================
4. Check if a number is divisible by both 3 and 5

def divisible(n):
    if n % 3 == 0 and n % 5 == 0:
        return f"{n} is divisible by 3 and 5"
    else:
        return "Not divisible"
    
print(divisible(10))
print(divisible(15))
==============================================================================================================================================================
5. Check leap year or not.

def solution(n):
    if n % 4 == 0:
        return f"{n} is a Leap year"
    elif n % 100 == 0 and n % 400 == 0:
        return f"{n} is a Leap year"
    else:
        return f"{n} is not a Leap year"

if __name__ == '__main__':
    n = 2021
    print(solution(n))
==============================================================================================================================================================
6. Take Two numbers and print Larger one.

def solution(num1, num2):
    if num1 > num2:
        return f"{num1} is Greater than {num2}."
    else:
        return f"{num2} is Greater than {num1}."

if __name__ == '__main__':
    num1 = 5
    num2 = 23
    print(solution(num1, num2))
==============================================================================================================================================================
7. Take Three numbers and print Largest.

def solution(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return f"{num1} is Greater than {num2} & {num3}."
    elif num2 > num1 and num2 > num3:
        return f"{num2} is Greater than {num1} & {num3}."
    else:
        return f"{num3} is Greater than {num1} & {num2}"
if __name__ == '__main__':
    num1 = 5
    num2 = 23
    num3 = 2
    print(solution(num1, num2, num3))
==============================================================================================================================================================
8.Take temp value and print "Cold", "Warm", "Hot" using range conditions.

def solution(temperature):
    if temperature <= -40:
        return f"Extreme Cold."
    elif temperature <= -15:
        return f"Very Cold"
    elif temperature <= 0:
        return f"Freezing point."
    elif temperature <= 10:
        return f"Cold Range."
    elif temperature <= 18:
        return f"Cold to Warm Boundary."
    elif temperature <= 25:
        return f"Comfortable Warm."
    elif temperature <= 30:
        return f"Warm to hot boundary."
    elif temperature <= 38:
        return f"Hot Temperature."
    elif temperature <= 50:
        return f"ver Hot"
    else:
        return f"Extreme Hot"


    
if __name__ == '__main__':
    temperature = -10
    print(solution(temperature))
==============================================================================================================================================================
9. Take a character and chack whether its vowel or consonant.

def solution(vowels, input):
    if not input.isalpha:
        return f"{input} is not a character"
    elif input.lower() in vowels:
        return f"{input} is a vowel."
    else:
        return f"{input} is a consonant."
    
if __name__ == '__main__':
    vowels = "aeiou"
    input = 's'
    print(solution(vowels, input))
==============================================================================================================================================================
10. Take a character and check whether its uppercase, lowercase, digit or special_character

def solution(entry):
    if entry.isdigit():
        return f"{entry} is a digit"
    elif entry.isupper():
        return f"{entry} is uppercase letter"
    elif entry.islower():
        return f"{entry} is lowercase letter"
    else:
        return f"{entry} is a Special character"
        
if __name__ == '__main__':
    entry = '@'
    print(solution(entry))
==============================================================================================================================================================
