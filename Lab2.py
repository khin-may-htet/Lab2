def display_main_menu():
    print("display_main_menu")

def get_user_input():
    user_input = input()

    string_list = user_input.split(",")

    float_list = []
    for num_str in string_list:
        float_list.append(float(num_str))

    return float_list

def calc_average_temperature(num_list):
    total = sum(num_list)
    average = total / len(num_list)
    return average

def calc_min_max_temperature(num_list):
    min = min(num_list)
    max = max(num_list)
    return [min,max]

def sort_temperature(num_list):
    sorted_list = sorted(num_list)
    return sorted_list

def calc_median_temperature(num_list):
    sorted_list = sort_temperature(num_list)
    length = len(sorted_list)

    if length % 2 == 0:
        mid1 =  length // 2-1
        mid2 = length // 2
        median = (sorted_list[mid1] + sorted_list[mid2]) / 2

    else:
        mid = length //2
        median = (sorted_list[mid])

    return median