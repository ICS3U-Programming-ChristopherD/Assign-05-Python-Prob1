#!/usr/bin/env python3

# Created By: Chris Di Bert
# Date: Dec. 9, 2022
# This program calculates the average acceleration of
# an object


# Function to calculate the average acceleration of an object
def average_acceleration_calculator(velocity_init, velocity_final, elapsed_time):

    # Returns the average acceleration of the object
    average_acceleration = (velocity_final - velocity_init) / elapsed_time
    return average_acceleration


# Function used to check for errors in the user's input or
# input that results in a special case
def exception_checker(velocity_init_str, velocity_final_str, elapsed_time_str):

    # Tries casting object properties to float
    try:
        velocity_init = float(velocity_init_str)
        velocity_final = float(velocity_final_str)
        elapsed_time = float(elapsed_time_str)

    # Returns casting error if casting was unsuccessful
    except:
        return -1

    # Return values for special cases
    else:
        if elapsed_time < 0:
            return -2

        elif elapsed_time == 0 and velocity_init > 0:
            return -3

        elif elapsed_time == 0 and velocity_final > 0:
            return -4

        elif elapsed_time == 0 and velocity_init == 0 and velocity_final == 0:
            return -5

        # Returns casted object properties if the inputs do not meet the conditions
        # for a special case
        else:
            return velocity_init, velocity_final, elapsed_time


def main():
    while True:
        print("\n\n\n\n\n\n")
        # Getting object properties from user
        units = input("Enter your units (cm, m, etc): ")
        velocity_init_user = input(f"Enter the object's initial velocity ({units}): ")
        velocity_final_user = input(f"Enter the object's final velocity ({units}): ")
        elapsed_time_user = input("Enter the elapsed time (seconds): ")

        # Checking for errors in user's input
        object_properties = exception_checker(
            velocity_init_user, velocity_final_user, elapsed_time_user
        )

        # Prints appropriate error/special case message
        # using return values from the exception checker
        match object_properties:

            # If the user did not enter a number for an input
            case -1:
                print("You must enter numbers for each input.")
                input("Enter any character to restart: ")
                continue

            # If the user entered time as a negative number
            case -2:
                print("Elapsed time cannot be negative.")
                input("Enter any character to restart: ")
                continue

            # If the time is set to 0 but initial velocity is a positive
            # number
            case -3:
                print("The average acceleration of the object is negatively infinity.")
                input("Enter any character to restart: ")
                continue

            # If the time is set to 0 but final velocity is a positive
            # number
            case -4:
                print("The average acceleration of the object is infinite.")
                input("Enter any character to restart: ")
                continue

            # If the user entered 0 for all inputs
            case -5:
                print("The object is not in motion.")
                input("Enter any character to restart: ")
                continue

        # Gets the average acceleration
        average_acceleration = average_acceleration_calculator(
            object_properties[0], object_properties[1], object_properties[2]
        )

        # Prints the average acceleration to the user then asks the user if they
        # would like to restart
        print(
            f"The average acceleration of the object is equal to {average_acceleration} {units}/s^2\n"
        )
        restart = input("Enter 'q' to quit. Enter any other key to restart.\n>> ")

        # Restarts if the user enters a null value
        if restart == "":
            continue

        # Exits if the user enters 'q'
        if restart[0].lower() == "q":
            break


if __name__ == "__main__":
    main()
