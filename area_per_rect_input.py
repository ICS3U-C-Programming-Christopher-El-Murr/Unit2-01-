#!/usr/bin/env python3
# Created By: Christopher El-Murr
# Date: 09 20, 2025
# This program is a basic math calculator capable of calculating the area and perimeter of a rectangle vVIA user input


score = int("5")
string = int("6")


def main():
    print("For a rectangle with length int and width string")
    print()
    print("The area is:{}cm^2".format(score * string))
    print("The perimeter is:{}cm".format(2 * (score + string)))


if __name__ == "__main__":
    main()
