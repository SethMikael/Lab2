import Lab2

print("Lab2 Test")


def test_find_min_max():
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    result = Lab2.find_min_max(input_arr)
    assert (result == [11, 90])


def test_calc_average():
    input_arr = [65, 34, 25, 12, 22, 11, 90]
    result = Lab2.calc_average(input_arr)
    assert (result == 37.0)

def test_calc_median_temperature():
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    result = Lab2.calc_median_temperature(input_arr)
    assert (result == 12)


