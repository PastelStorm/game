import random
import sys
import webbrowser

def math():
    print 'Math test'
    num1 = random.randint(10, 100)
    num2 = random.randint(10, 100)
    print 'How much is %d + %d' % (num1, num2)
    while True:
        answer = raw_input('Enter your answer please:')
        try:
            answer = int(answer)
            break
        except ValueError:
            print "Numbers only. Try again."

    if int(answer) == num1 + num2:
        print 'Correct!!! Well done.'
    else:
        print 'Wrong answer.'

def logic():
    print 'Logic test.'
    while True:
        age = raw_input('How old are you?')
        try: 
           age == int(age)
           break
        except ValueError:
           print 'Numbers only, ex: 33'

    print 'If you are a pilot of a plane and the plane flys 1000000 mph what is the age of the pilot'
    while True:   
        answer = raw_input('Guess the age of the pilot:')
        try:
            answer == int(answer)
            break
        except ValueError:
            print 'Numbers only. Try again'    

    if int(answer) == int(age):
        print 'Correct!!!'
        webbrowser.open("http://upload.wikimedia.org/wikipedia/commons/thumb/0/0b/Champions_2009.JPG/1280px-Champions_2009.JPG")
    else:
        print 'Wrong, correct answer is', age, '.'

def welcome():
    print 'Hello, what is your name?'
    name = raw_input('')
    if name.isdigit() == True:
        print 'Strange name, but anyway'
    print 'it is good to meet you ' + name.capitalize(), '.'

if __name__ == "__main__":
    welcome()
    math()
    logic()
