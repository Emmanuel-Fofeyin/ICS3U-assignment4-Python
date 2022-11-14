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
        if x_number == y_number == z_number:
            print(
                "\nThe angles {0} {1} and {2} make an Equilateral triangle!".format(
                    x_string, y_string, z_string
                )
            )
        elif x_number == y_number or y_number == z_number or x_number == z_number:
            print(
                "\nThe angles {0} {1} and {2} make an Isosceles triangle!".format(
                    x_string, y_string, z_string
                )
            )
        else:
            print(
                "\nThe angles {0} {1} and {2} make a Scalene triangle!".format(
                    x_string, y_string, z_string
                )
            )
    except ValueError:
        print("\nSorry This is invalid input")
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()
