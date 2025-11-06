def move(my_list, direction):
    if 1 not in my_list:
        return my_list  # אין מה להזיז

    new_list = my_list[:]  # העתקה של הרשימה
    index_of_one = new_list.index(1)

    if direction == 'right' and index_of_one < len(new_list) - 1:
        new_list[index_of_one] = 0
        new_list[index_of_one + 1] = 1

    elif direction == 'left' and index_of_one > 0:
        new_list[index_of_one] = 0
        new_list[index_of_one - 1] = 1

    return new_list
