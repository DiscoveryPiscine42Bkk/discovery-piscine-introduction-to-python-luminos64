#!/usr/bin/env python3

def greetings(name=None):
    if not name:
        print("Hello, noble stranger.")
    else:
        if isinstance(name, int):
            print("Error! It was not a name.")
        else:
            print("Hello,", name)
        # try:
        #     name = int(name)
        #     print("Error! It was not a name.")
        # except:
        #     name = str(name)
        #     print("Hello,", name)


greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)
