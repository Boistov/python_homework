def find_in(my_list, max_val):
    if len(my_list) <= 1:
        return max_val
    else:
        if my_list[0] > max_val:
            return find_in(my_list[1:], my_list[0])
        else:
            return find_in(my_list[1:], max_val)

if __name__ == '__main__':
    my_list = [1, 5, 16, 9, 20, 40, 5]
    print(find_in(my_list, my_list[0]))
