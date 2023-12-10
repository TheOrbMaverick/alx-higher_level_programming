#!/usr/bin/python3
import hidden_4

if __name == "__main__":
    for i in dir(hidden_4):
        if i[0:4] != "__":
            print("{:s}".format(i))
