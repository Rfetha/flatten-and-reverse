flattened_list = []
def flatten(input_list):
    for i in input_list:
        if type(i) != list:
            flattened_list.append(i)
        else:
            flatten(i)
        return flattened_list


reversed_list = []
def reverse(input_list):
    for i in input_list:
        i.reverse()
        reversed_list.append(i)
    reversed_list.reverse()
    return reversed_list

