def countdown(number=5):
    count = 0
    count_list = []
    while number >= count:
        count_list += [number]
        number -= 1
    return count_list
print(countdown())

def print_and_return(number):
    print(number[0])
    return(number[1])
print_and_return([1,2])
new_return = print_and_return([1,2])
print(new_return)

def first_plus_length(number):
    sum = number[0] + len(number)
    return(sum)
new_sum = first_plus_length([1,2,3,4,5])
print(new_sum)

def values_greater_than_second(list):
    if len(list) < 2:
        return False
    new_list = []
    for number in list:
        if number > list[1]:
            new_list += [number]
    print(len(new_list))
    return new_list
greater_values = values_greater_than_second([5,2,3,2,1,4])
print(greater_values)
nada = values_greater_than_second([3])
print(nada)

def length_and_value(repeat, integer):
    list = []
    list += [integer] * repeat
    return list
first_list = length_and_value(4,7)
print(first_list)
second_list = length_and_value(6,2)
print(second_list)