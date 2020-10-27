import time

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
    else :
        wait()
        print('I don\'t understand.')
    
