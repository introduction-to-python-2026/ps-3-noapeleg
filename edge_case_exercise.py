def move(my_list, direction):
    # יוצרים עותק חדש של הרשימה כדי לא לשנות את המקורית
    new_list = my_list.copy()

    # מוצאים את המיקום של המספר 1
    index_of_one = new_list.index(1)

    # אם הכיוון הוא ימין, ומותר לזוז (לא בקצה הימני)
    if direction == "right" and index_of_one < len(new_list) - 1:
        new_list[index_of_one] = 0
        new_list[index_of_one + 1] = 1

    # אם הכיוון הוא שמאל, ומותר לזוז (לא בקצה השמאלי)
    elif direction == "left" and index_of_one > 0:
        new_list[index_of_one] = 0
        new_list[index_of_one - 1] = 1

    # מחזירים את הרשימה החדשה
    return new_list
