import ast
import math
import numpy as np

with open('day13input.txt') as reader:
    lines = reader.readlines()

input_data = [line for line in lines]


def xor(x,y):
    return bool((x and not y) or (not x and y))

def compare(item1, item2):
    if isinstance(item1, int) and isinstance(item2, int):
        return compare_ints(item1, item2)
    if isinstance(item1, int) and isinstance(item2, list) or isinstance(item1, list) and isinstance(item2, int):
        return single_int(item1, item2)
    if isinstance(item1, list) and isinstance(item2, list):
        return compare_lists(item1, item2)

def compare_ints(int1, int2):
    if int1 < int2:
        return True
    elif int2 < int1:
        return False
    else:
        return None

def single_int(left, right):
    if isinstance(left, int):
        return compare_lists([left], right)
    else:
        return compare_lists(left,[right])

def compare_lists(list1, list2):
    if xor(len(list1) == 0, len(list2) == 0):
        if len(list1) == 0:
            return True
        else:
            return False
    if len(list1) == 0 and len(list2) == 0:
        return None
    item1 = list1[0]
    item2 = list2[0]
    if isinstance(item1, int):
        if isinstance(item2, int):
            test = compare_ints(item1, item2)
            if test:
                return True
            elif test == False:
                return False
            else:
                value =  compare_lists(list1[1:len(list1)],list2[1:len(list2)])
                if value:
                    return True
                elif value == False:
                    return False
        if isinstance(item2, list):
            if [item1] == item2:
                return compare(list1[1:len(list1)],list2[1:len(list2)])
            else:
                return compare_lists([item1],item2)
    if isinstance(item1, list):
        if isinstance(item2, int):
            if item1 == [item2]:
                return compare(list1[1:len(list1)],list2[1:len(list2)])
            else:
                return compare_lists(item1,[item2])
        if isinstance(item2, list):
            if item1 == item2:
                return compare(list1[1:len(list1)],list2[1:len(list2)])
            else:
                return compare_lists(item1,item2)

       
a = 0
for x in range(0,len(input_data), 3):
    line1= ast.literal_eval(input_data[x])
    line2 = ast.literal_eval(input_data[x+1])
    index=math.floor((x)/3)+1
    correct_order = compare(line1,line2)
    if correct_order:
        a += index
print('part 1: ' + str(a))



ordered_list = [[[2]],[[6]]]
for x in range(len(input_data)):
	line = ast.literal_eval(input_data[x])
	for y in range(len(ordered_list)):
		packet = ordered_list[y]
		order = compare(packet, line)
		if order == False:
			ordered_list.insert(y,line)
			break
		if y == len(ordered_list)-1:
			ordered_list.append(line)

index_1 = ordered_list.index([[2]])+1
index_2 = ordered_list.index([[6]])+1
product = index_1 * index_2
print(product)