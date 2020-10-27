import time
import random
def wait(delay=3):
    for i in range(delay):
        print('.')
        time.sleep(1)

while True:
    text = input('Put down some text ')
    if text=='Hello':
        wait()
        print ('Hello.I\'m CatBot.')
    elif text=='I\'m hungry':
        wait()        
        print ('I\'m too.')

    elif text=='Are you a human?':
        wait()
        print ('I\'m not human.')
    elif text=='Exit':
        wait()
        print ('Goodbye')
        exit (0)
    elif text=='Do you speak to Russian?':
        wait()
        print ('No')
    elif text=='Who you?':
        wait()
        print ('I\'m a program.')
    elif text=='Do you speak to English?':
        wait()
        print ('Yes')
    elif text=='What can you do?':
        wait()
        print('Print')
    elif text=='Let\'s play?')
        wait()
        print('Yes')
               wait()
        r=random.randint(1,3)
        if r==1 :
            print ('He meows')
            print ('1.It is a cat?')
            wait()
            print ('2.Is it an smartphone?')
            wait()
            print ('3.He is a builder?')
            wait()
            text = int(input('Choose an answer '))
        if text==1:
            wait()
            print('Yes.It is a cat.')
        elif text==2:
            wait()
            print('No.')
        elif text==3:
            wait()
            print('No.')
    elif r==2 :
        print('This is a device')
        print ('1.It is a dog?')
        wait()
        print ('2.It is an computer?')
        wait()
        print ('3.He is a teacher?')
        wait()
        text = int(input('Choose an answer '))
        if text==1:
            wait()
            print('No.')
        elif text==2:
            wait()
            print('Yes.It is a computer.')
            exit(0)
        elif text==3:
            wait()
            print('No.')
    elif r==3 :
        print('He programms')
        print ('1.It is an plane?')
        wait()
        print ('2.He is a programmer?')
        wait()
        print ('3.It is a rat?')
        wait()
        text = int(input('Choose an answer '))
        if text==1:
            wait()
            print('No.')
        elif text==2:
            wait()
            print('Yes.He is a programmer')
            exit(0)
        elif text==3:
            wait()
            print('No.')
    else :
        wait()
        print('I don\'t understand.')
    
