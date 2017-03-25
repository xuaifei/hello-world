"""this is a test project"""

import os

if __name__ == '__main__':
    print(os.getcwd())
    print __doc__

    print(123)

    a = 123

    b = 456

    print("hello")

    print("test git")

    name = raw_input("enter name:")
    outputstr = "your name %s" % name
    print(outputstr)