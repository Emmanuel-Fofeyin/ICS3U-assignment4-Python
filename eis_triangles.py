#!/usr/bin/env python3

# Created by: Emmanuel
# Created on: Nov 2022
# This program determines if a triangle is a Scalene,
# Equilateral, or Isosceles triangle.


def main():
    # In this program the letters x,y and z represent the three angle in a triangle.

    # input
    x_string = input("Enter in the 1st angle: ")
    y_string = input("Enter in the 2nd angle: ")
    z_string = input("Enter in a 3rd angle: ")

    # process and output
    try:
        x_number = int(x_string)
        y_number = int(y_string)
        z_number = int(z_string)
        if (
            x_number + y_number + z_number == 180
            and x_number > 0
            and y_number > 0
            and z_number > 0
        ):
            if x_number == y_number and y_number == z_number and z_number == x_number:
                print("\nThese angles make an Equilateral triangle!")
            elif x_number == y_number or y_number == z_number or x_number == z_number:
                print("\nThese angles make an Isosceles triangle!")
            else:
                print("These angles make a Scalene triangle!")
        else:
            print("This is not a triangle")
    except ValueError:
        print("\nSorry This is invalid input")
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
