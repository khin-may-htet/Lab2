def display_main_menu():
    print("display_main_menu")

def get_use_input():
    uset_input = input()

    string_list = user_input.split(",")

    float_list = []
    for item in string_list:
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