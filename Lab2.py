print("ET0735 (DevOPS for AIOT) - Lab 2 - Introduction to Python \n\n")
array = []


def display_main_menu():
    print("\n\nEnter some numbers, separated by commas: (eg 5, 67, 32)")


def get_user_input():
    userinput = input("——> ")
    userinput = userinput.split(",")
    for i in userinput:
        converted_userinput = float(i)
        array.append(converted_userinput)
    return array


def calc_average():
    average = sum(array) / len(array)
    print("Average = " + str(average))


def find_min_max():
    print("Min = " + str(min(array)))
    print("Max = " + str(max(array)))


def sort_temperature():
    array.sort()
    print("Sorted = " + str(array))


def calc_median_temperature():
    median = len(array) // 2
    print("Median = " + str(array[median]))


def calc_min_max_temperature():
    print("Min = " + str(min(array)))
    print("Max = " + str(max(array)))


def choose_menu():
    print("Choose menu:")
    print("1. Number")
    print("2. Temperature")
    option = input("——> ")
    if option == "1":
        display_main_menu()
        get_user_input()
        print("\n\n")
        calc_average()
        find_min_max()

    elif option == "2":
        print("\n\nEnter some temperatures, separated by commas: (eg 5, 67, 32)")
        get_user_input()
        print("\n\n")
        sort_temperature()
        calc_average()
        calc_min_max_temperature()
        calc_median_temperature()


def main():
    choose_menu()


main()