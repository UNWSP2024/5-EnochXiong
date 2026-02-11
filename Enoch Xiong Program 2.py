import random

def math_quiz():
    number1 = random.randint(1,999 )
    number2 = random.randint(1,999 )

    print(' ', number1)
    print('+', number2)
    print('------------')

    answer = int(input("Enter a number: "))

    Canswer = number1 + number2

    if answer == Canswer:
        print('You are correct')
    else:
        print('Wrong answer, the correct answer is:', Canswer)
if __name__ == '__main__':
    math_quiz()
