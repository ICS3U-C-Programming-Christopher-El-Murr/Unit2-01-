#!/usr/bin/env python3
# Created By: Christopher El-Murr
# Date: 09 18, 2025
# This program is a basic math calculator capable of calculating the area and perimeter of a rectangle

#Enter values below
length = 6
width = 4


def main():
    print("For a rectangle with length (length) cm and width (width) cm")
    print()
    print("The area is:{}cm^2".format((length) * (width)))
    print("The perimeter is:{}cm".format(2 * ((length) + (width))))


if __name__ == "__main__":
    main()
