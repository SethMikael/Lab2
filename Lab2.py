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


def calc_average(array):
    average = sum(array) / len(array)
    print("Average = " + str(average))
    return average


def find_min_max(array):
    print("Min = " + str(min(array)))
    print("Max = " + str(max(array)))
    return [min(array), max(array)]


def sort_temperature():
    array.sort()
    print("Sorted = " + str(array))


def calc_median_temperature(array):
    median = len(array) // 2
    print("Median = " + str(array[median]))
    return array[median]


def calc_min_max_temperature():
    int_array = [int(i) for i in array]
    print("Min = " + str(min(int_array)))
    print("Max = " + str(max(int_array)))


