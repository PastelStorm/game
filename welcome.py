import random


def math():
    print 'Math test'
    num1 = random.randint(10, 80)
    num2 = random.randint(10, 80)
    print 'How much is %d + %d' % (num1, num2)
    no_num = 0
    while True:
        answer = raw_input('Enter your answer please:')
        no_num += 1
        if answer.isdigit():
            break
        elif no_num == 3:
            print "Game over"
            return None
        else:
            print "Numbers only. Try again"

    if int(answer) == num1 + num2:
        print 'Correct!!!'
    else:
        print 'Wrong answer'
        
def logic():
    print 'Logic test'
    while True:
        age = raw_input('How old are you?')
        if age.isdigit():
            break
        else:
            print 'Numbers only'
    print 'If you are a pilot of a plane and the plane flys 1000 mph what is the age of the pilot'
    while True: 
        answer = raw_input('Guess the age of the pilot:')
        if answer.isdigit():
            break
        else:
            print 'Numbers only. Try again' 
    if answer == age:
        print 'Correct!!!'
    else:
        print "%s %s" % ("Wrong, correct answer is", age)

def welcome():
    print 'Hello, what is your name?'
    name = raw_input('')
    if name.isdigit():
        print 'Strange name, but anyway'
    print 'It is good to meet you ' + name.capitalize()

if __name__ == "__main__":
    #welcome()
    math()
    #logic()
